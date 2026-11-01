SKILL_DIR ?= $(HOME)/.config/opencode/skills/super-mega-brainstorm-skill
DIST ?= dist/super-mega-brainstorm-skill-0.2.0.zip

.PHONY: test validate lint checker check install package clean

test:
	bash tests/run_tests.sh

validate:
	python3 scripts/validate_package.py .

lint:
	python3 scripts/lint_output.py tests/fixtures/valid_creative.md --mode workshop
	python3 scripts/lint_output.py tests/fixtures/valid_workshop.md --mode workshop
	python3 scripts/lint_output.py tests/fixtures/valid_false_premise.md --mode deep
	python3 scripts/lint_output.py tests/fixtures/valid_one_solution.md --mode workshop
	python3 scripts/lint_output.py tests/fixtures/valid_zero_solution.md --mode workshop

checker:
	python3 scripts/argument_checker.py --premise "P -> Q" --premise "P" --conclusion "Q"
	python3 scripts/argument_checker.py --premise "P -> Q" --premise "Q" --conclusion "P" || test $$? -eq 1
	python3 scripts/categorical_checker.py --premise "All M are P" --premise "All S are M" --conclusion "All S are P"
	python3 scripts/categorical_checker.py --premise "All P are M" --premise "All S are M" --conclusion "All S are P" || test $$? -eq 1

check: validate test lint checker

install: clean
	mkdir -p "$(SKILL_DIR)"
	cp SKILL.md README.md MIGRATION.md CHANGELOG.md PRODUCT_REQUIREMENTS.md DECISION_LOG.md PROJECT_STATUS.md Makefile .gitignore "$(SKILL_DIR)/"
	cp -R references assets scripts tests docs .github "$(SKILL_DIR)/"

package: clean
	mkdir -p dist
	rm -f "$(DIST)"
	cd .. && zip -r "super-mega-brainstorm-skill/$(DIST)" super-mega-brainstorm-skill \
		-x 'super-mega-brainstorm-skill/.git/*' \
		   'super-mega-brainstorm-skill/.git-that-shit/*' \
		   'super-mega-brainstorm-skill/.opencode/*' \
		   'super-mega-brainstorm-skill/**/__pycache__/*' \
		   'super-mega-brainstorm-skill/**/*.pyc' \
		   'super-mega-brainstorm-skill/dist/*' \
		   'super-mega-brainstorm-skill/docs/test-results.txt' \
		   'super-mega-brainstorm-skill/docs/validation.json' \
		   'super-mega-brainstorm-skill/docs/install-test.txt' \
		   'super-mega-brainstorm-skill/docs/argument-checker-results.txt' \
		   'super-mega-brainstorm-skill/docs/zip-test.txt'

clean:
	find scripts tests references assets docs -type d -name __pycache__ -prune -exec rm -rf {} +
	find scripts tests references assets docs -type f -name '*.pyc' -delete
