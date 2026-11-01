#!/usr/bin/env python3
"""Finite propositional-validity checker. No external dependencies.

This verifies abstract inference only, not natural-language translation or premise truth.
Operators: !, &, |, ->, parentheses. Priority: !, &, |, -> (right-associative).
"""
import argparse
import itertools
import json
import re

TOKENS = re.compile(r'\s*(->|[()!&|]|[A-Za-z][A-Za-z0-9_]*)')

class FormulaError(ValueError):
    pass


def tokenize(text):
    items = []
    pos = 0
    while pos < len(text):
        m = TOKENS.match(text, pos)
        if not m:
            if not text[pos:].strip():
                break
            raise FormulaError(f"Unexpected character at {pos}: {text[pos:pos+14]!r}")
        items.append(m.group(1))
        pos = m.end()
    if not items:
        raise FormulaError('Empty formula')
    return items


class Parser:
    def __init__(self, text):
        self.items = tokenize(text)
        self.index = 0

    def peek(self):
        return self.items[self.index] if self.index < len(self.items) else None

    def pop(self, wanted=None):
        value = self.peek()
        if value is None or (wanted is not None and value != wanted):
            raise FormulaError(f'Expected {wanted or "token"}, got {value}')
        self.index += 1
        return value

    def atom(self):
        t = self.peek()
        if t == '!':
            self.pop('!')
            return ('not', self.atom())
        if t == '(':
            self.pop('(')
            node = self.implication()
            self.pop(')')
            return node
        if t and re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', t):
            self.pop()
            if t.upper() in ('AND', 'OR', 'NOT', 'TRUE', 'FALSE'):
                raise FormulaError('Use symbols ! & |, not word operators')
            return ('var', t)
        raise FormulaError(f'Expected variable, !, or (, got {t}')

    def conjunction(self):
        v = self.atom()
        while self.peek() == '&':
            self.pop('&')
            v = ('and', v, self.atom())
        return v

    def disjunction(self):
        v = self.conjunction()
        while self.peek() == '|':
            self.pop('|')
            v = ('or', v, self.conjunction())
        return v

    def implication(self):
        v = self.disjunction()
        if self.peek() == '->':
            self.pop('->')
            return ('implies', v, self.implication())
        return v

    def parse(self):
        tree = self.implication()
        if self.peek() is not None:
            raise FormulaError(f'Unexpected trailing token: {self.peek()}')
        return tree


def variables(tree):
    if tree[0] == 'var':
        return {tree[1]}
    return set().union(*(variables(x) for x in tree[1:] if isinstance(x, tuple)))


def evaluate(t, env):
    op = t[0]
    if op == 'var': return env[t[1]]
    if op == 'not': return not evaluate(t[1], env)
    if op == 'and': return evaluate(t[1], env) and evaluate(t[2], env)
    if op == 'or': return evaluate(t[1], env) or evaluate(t[2], env)
    if op == 'implies': return (not evaluate(t[1], env)) or evaluate(t[2], env)
    raise FormulaError(f'Unknown operator {op}')


def check(premises, conclusion, max_vars=12):
    if not premises:
        raise FormulaError('At least one premise required')
    trees = [Parser(p).parse() for p in premises]
    goal = Parser(conclusion).parse()
    atoms = sorted(set().union(*(variables(t) for t in [*trees, goal])))
    if len(atoms) > max_vars:
        raise FormulaError(f'Too many atomic propositions ({len(atoms)}); cap {max_vars}')
    for vals in itertools.product((False, True), repeat=len(atoms)):
        env = dict(zip(atoms, vals))
        if all(evaluate(t, env) for t in trees) and not evaluate(goal, env):
            return {'verdict': 'INVALID', 'counterexample': env, 'atoms': atoms, 'note': 'Formalization only; premise truth not tested'}
    return {'verdict': 'VALID', 'counterexample': None, 'atoms': atoms, 'note': 'Formalization only; premise truth not tested'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--premise', action='append', required=True)
    p.add_argument('--conclusion', required=True)
    p.add_argument('--json', action='store_true')
    args = p.parse_args()
    try:
        result = check(args.premise, args.conclusion)
    except FormulaError as ex:
        p.error(str(ex))
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(result['verdict'])
        if result['counterexample'] is not None:
            print('Counterexample:', ', '.join(f'{k}={v}' for k,v in result['counterexample'].items()))
        print(result['note'])

if __name__ == '__main__':
    main()
