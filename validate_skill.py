#!/usr/bin/env python3
"""
Brainstorm Skill Validator

A lightweight, dependency-free validation script using Python's standard library.
Validates the Brainstorm Agent Skill package structure and content.
"""

import os
import sys
import re
import yaml
from pathlib import Path


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


class SkillValidator:
    """Validates a Brainstorm Agent Skill package."""
    
    REQUIRED_FILES = [
        'SKILL.md',
        'references/techniques.md',
        'README.md',
    ]
    
    OPTIONAL_FILES = [
        'CHANGELOG.md',
        'adapters/chatgpt.md',
        'adapters/codex.md',
        'adapters/claude.md',
        'adapters/mistral.md',
        'adapters/opencode.md',
        'tests/acceptance.md',
    ]
    
    REQUIRED_METADATA = ['name', 'description']
    
    REQUIRED_SECTIONS = [
        'When to activate',
        'Operating principles',
        'Modes',
        'Workflow',
        'Output contract',
        'Hard rules',
        'Technique quick-pick',
    ]
    
    OUTPUT_CONTRACT_SECTIONS = [
        'Framing',
        'Options',
        'Kill list',
        'Ranking',
        'Next action',
    ]
    
    OPERATING_MODES = ['QUICK', 'STANDARD', 'DEEP']
    
    def __init__(self, skill_path=None):
        """Initialize validator with optional skill path."""
        self.skill_path = Path(skill_path) if skill_path else Path.cwd()
        self.errors = []
        self.warnings = []
        self.info = []
    
    def validate(self):
        """Run all validation checks."""
        self.info.append(f"Validating skill at: {self.skill_path.resolve()}")
        
        self._check_directory_structure()
        self._check_required_files()
        self._check_skill_md()
        self._check_techniques_md()
        self._check_internal_references()
        self._check_name_consistency()
        self._check_no_license()
        self._check_no_proprietary_deps()
        
        return {
            'valid': len(self.errors) == 0,
            'errors': self.errors,
            'warnings': self.warnings,
            'info': self.info,
        }
    
    def _check_directory_structure(self):
        """Check that the directory structure is correct."""
        if not self.skill_path.exists():
            self.errors.append(f"Skill directory not found: {self.skill_path}")
            return
        
        if not self.skill_path.is_dir():
            self.errors.append(f"Path is not a directory: {self.skill_path}")
            return
        
        # Check directory name
        if self.skill_path.name != 'brainstorm':
            self.warnings.append(
                f"Directory name '{self.skill_path.name}' should be 'brainstorm' "
                f"to match skill name"
            )
    
    def _check_required_files(self):
        """Check that all required files exist."""
        for file_path in self.REQUIRED_FILES:
            full_path = self.skill_path / file_path
            if not full_path.exists():
                self.errors.append(f"Missing required file: {file_path}")
            else:
                self.info.append(f"Found required file: {file_path}")
        
        # Check optional files
        for file_path in self.OPTIONAL_FILES:
            full_path = self.skill_path / file_path
            if full_path.exists():
                self.info.append(f"Found optional file: {file_path}")
    
    def _check_skill_md(self):
        """Validate SKILL.md content."""
        skill_md = self.skill_path / 'SKILL.md'
        if not skill_md.exists():
            return  # Error already reported
        
        content = skill_md.read_text(encoding='utf-8')
        
        # Check YAML frontmatter
        self._check_yaml_frontmatter(content)
        
        # Check required sections
        self._check_required_sections(content)
        
        # Check output contract
        self._check_output_contract(content)
        
        # Check operating modes
        self._check_operating_modes(content)
        
        # Check for constraint line pattern
        self._check_constraint_pattern(content)
        
        # Check for absurd idea requirement
        self._check_absurd_idea(content)
    
    def _check_yaml_frontmatter(self, content):
        """Validate YAML frontmatter."""
        # Check for frontmatter delimiters
        if not content.startswith('---'):
            self.errors.append("SKILL.md: Missing YAML frontmatter opening delimiter '---'")
            return
        
        # Find the end of frontmatter
        lines = content.split('\n')
        if len(lines) < 2 or not lines[0].startswith('---'):
            self.errors.append("SKILL.md: Invalid frontmatter format")
            return
        
        # Extract frontmatter
        frontmatter_lines = []
        in_frontmatter = False
        for line in lines:
            if line.strip() == '---':
                if in_frontmatter:
                    break
                in_frontmatter = True
                continue
            if in_frontmatter:
                frontmatter_lines.append(line)
        
        frontmatter = '\n'.join(frontmatter_lines)
        
        # Try to parse YAML (basic check - full validation requires PyYAML)
        try:
            # Simple check: does it look like YAML?
            if ':' not in frontmatter:
                self.warnings.append("SKILL.md: Frontmatter doesn't contain key-value pairs")
            
            # Check for required metadata
            for field in self.REQUIRED_METADATA:
                if f'{field}:' not in frontmatter.lower():
                    self.errors.append(f"SKILL.md: Missing required metadata field: {field}")
            
            # Check name field
            if 'name: brainstorm' not in frontmatter.lower():
                self.warnings.append(
                    "SKILL.md: name field should be 'brainstorm' "
                    "(case-insensitive check)"
                )
            
            # Check description field
            if 'description:' not in frontmatter.lower():
                self.errors.append("SKILL.md: Missing description field")
            
        except Exception as e:
            self.warnings.append(f"SKILL.md: Error parsing frontmatter: {e}")
    
    def _check_required_sections(self, content):
        """Check that required sections exist in SKILL.md."""
        for section in self.REQUIRED_SECTIONS:
            if section not in content:
                self.errors.append(f"SKILL.md: Missing required section: {section}")
            else:
                self.info.append(f"SKILL.md: Found section: {section}")
    
    def _check_output_contract(self, content):
        """Check that all five output contract sections are defined."""
        missing_sections = []
        for section in self.OUTPUT_CONTRACT_SECTIONS:
            if section not in content:
                missing_sections.append(section)
        
        if missing_sections:
            self.errors.append(
                f"SKILL.md: Missing output contract sections: "
                f"{', '.join(missing_sections)}"
            )
        else:
            self.info.append("SKILL.md: All five output contract sections found")
    
    def _check_operating_modes(self, content):
        """Check that all three operating modes are mentioned."""
        missing_modes = []
        for mode in self.OPERATING_MODES:
            if mode not in content:
                missing_modes.append(mode)
        
        if missing_modes:
            self.errors.append(
                f"SKILL.md: Missing operating modes: {', '.join(missing_modes)}"
            )
        else:
            self.info.append("SKILL.md: All three operating modes (QUICK, STANDARD, DEEP) found")
    
    def _check_constraint_pattern(self, content):
        """Check for the constraint line pattern."""
        # Look for the pattern: Costs: ... · Gives up: ... · Needs: ...
        pattern = r'Costs:\s*.+\s*\·\s*Gives up:\s*.+\s*\·\s*Needs:'
        if not re.search(pattern, content):
            self.warnings.append(
                "SKILL.md: Could not find constraint line pattern "
                "(Costs: ... · Gives up: ... · Needs: ...)"
            )
        else:
            self.info.append("SKILL.md: Constraint line pattern found")
    
    def _check_absurd_idea(self, content):
        """Check that absurd idea requirement is documented."""
        if 'absurd' not in content.lower():
            self.errors.append("SKILL.md: No mention of absurd idea requirement")
        elif 'exactly one' not in content.lower() and 'one absurd' not in content.lower():
            self.warnings.append(
                "SKILL.md: Absurd idea mentioned but 'exactly one' requirement unclear"
            )
        else:
            self.info.append("SKILL.md: Absurd idea requirement found")
    
    def _check_techniques_md(self):
        """Validate techniques.md content."""
        techniques_md = self.skill_path / 'references' / 'techniques.md'
        if not techniques_md.exists():
            return  # Error already reported
        
        content = techniques_md.read_text(encoding='utf-8')
        
        # Check for expected sections
        expected_sections = [
            'Problem Framing Techniques',
            'Idea Generation Techniques',
            'Perspective Shifting Techniques',
            'Decision and Convergence Techniques',
        ]
        
        for section in expected_sections:
            if section not in content:
                self.warnings.append(
                    f"references/techniques.md: Missing expected section: {section}"
                )
            else:
                self.info.append(
                    f"references/techniques.md: Found section: {section}"
                )
        
        # Check for technique codes (A1, B2, etc.)
        technique_pattern = r'[A-Z]\d+'
        techniques_found = re.findall(technique_pattern, content)
        if len(techniques_found) < 10:
            self.warnings.append(
                f"references/techniques.md: Only found {len(techniques_found)} "
                f"technique codes (expected 20+)"
            )
        else:
            self.info.append(
                f"references/techniques.md: Found {len(techniques_found)} "
                f"technique codes"
            )
    
    def _check_internal_references(self):
        """Check that internal Markdown references resolve."""
        skill_md = self.skill_path / 'SKILL.md'
        if not skill_md.exists():
            return
        
        content = skill_md.read_text(encoding='utf-8')
        
        # Find all Markdown links
        link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
        links = re.findall(link_pattern, content)
        
        for link_text, link_path in links:
            # Skip external links
            if link_path.startswith(('http://', 'https://', 'mailto:')):
                continue
            
            # Skip anchor links
            if link_path.startswith('#'):
                continue
            
            # Check if relative file exists
            full_path = (self.skill_path / link_path).resolve()
            if not full_path.exists():
                self.warnings.append(
                    f"SKILL.md: Broken internal link: [{link_text}]({link_path}) "
                    f"- target not found: {full_path}"
                )
            else:
                self.info.append(
                    f"SKILL.md: Internal link OK: [{link_text}]({link_path})"
                )
    
    def _check_name_consistency(self):
        """Check that directory name matches skill name in SKILL.md."""
        skill_md = self.skill_path / 'SKILL.md'
        if not skill_md.exists():
            return
        
        content = skill_md.read_text(encoding='utf-8')
        
        # Extract name from frontmatter
        name_match = re.search(r'^name:\s*(\S+)', content, re.MULTILINE | re.IGNORECASE)
        if not name_match:
            self.warnings.append("Could not extract skill name from frontmatter")
            return
        
        skill_name = name_match.group(1).strip()
        
        if skill_name.lower() != 'brainstorm':
            self.errors.append(
                f"Skill name in frontmatter ('{skill_name}') "
                f"does not match expected 'brainstorm'"
            )
        elif self.skill_path.name != 'brainstorm':
            self.errors.append(
                f"Directory name ('{self.skill_path.name}') "
                f"does not match skill name 'brainstorm'"
            )
        else:
            self.info.append("Directory name matches skill name: brainstorm")
    
    def _check_no_license(self):
        """Check that no license file or license headers exist."""
        # Check for license files
        license_files = [
            'LICENSE', 'LICENSE.md', 'LICENSE.txt',
            'COPYING', 'COPYING.md',
            'license', 'copying',
        ]
        
        for lf in license_files:
            lf_path = self.skill_path / lf
            if lf_path.exists():
                self.warnings.append(f"Found license file: {lf} (should be removed per requirements)")
        
        # Check for SPDX identifiers in files
        # But allow phrases like "No license has been assigned" or empty license field
        for md_file in ['SKILL.md', 'README.md']:
            file_path = self.skill_path / md_file
            if file_path.exists():
                content = file_path.read_text(encoding='utf-8')
                # Look for SPDX identifiers that aren't part of "no license" statements
                spdx_pattern = r'\b(MIT|Apache|GPL|AGPL|BSD|ISC|Unlicense|CC|Creative\s+Commons)\b'
                matches = re.finditer(spdx_pattern, content, re.IGNORECASE)
                for match in matches:
                    # Check context around the match
                    start = match.start()
                    context = content[max(0, start - 50):start + 50]
                    # If it's not in a "no license" or "not licensed" context, warn
                    # Also allow empty license field: license: ""
                    if 'no license' not in context.lower() and \
                       'not licensed' not in context.lower() and \
                       'license: ""' not in context and \
                       'license:' not in context:
                        self.warnings.append(
                            f"{md_file}: Found license identifier '{match.group()}' "
                            f"(should be removed per requirements)"
                        )
                        break  # Only report first occurrence per file
    
    def _check_no_proprietary_deps(self):
        """Check for proprietary dependencies in documentation."""
        files_to_check = ['SKILL.md', 'README.md', 'references/techniques.md']
        
        # Patterns that indicate proprietary dependencies
        proprietary_patterns = [
            r'api[._-]?key',
            r'api[._-]?secret',
            r'authentication[._-]?token',
            r'access[._-]?token',
            r'private[._-]?key',
            r'secret[._-]?key',
            r'credentials?',
            r'password',
            r'[Aa]PI[._-]?[Kk]ey',
        ]
        
        # Patterns that are OK in documentation (describing what NOT to do)
        # These are allowed in the context of methodology description
        allowed_patterns = [
            r'proprietary',  # Used in "no proprietary dependencies"
            r'paid[._-]?service',  # Used in descriptions
            r'subscription',  # Used in descriptions
        ]
        
        for file_path in files_to_check:
            full_path = self.skill_path / file_path
            if full_path.exists():
                content = full_path.read_text(encoding='utf-8')
                for pattern in proprietary_patterns:
                    match = re.search(pattern, content, re.IGNORECASE)
                    if match:
                        # Check if it's in a "don't do" context
                        start = match.start()
                        context = content[max(0, start - 100):start + 100]
                        if 'do not' not in context.lower() and "don't" not in context.lower() and 'not' not in context.lower():
                            self.warnings.append(
                                f"{file_path}: Found potential proprietary dependency reference: "
                                f"{pattern}"
                            )


def print_validation_results(results):
    """Print validation results in a readable format."""
    print("=" * 70)
    print("BRAINSTORM SKILL VALIDATION REPORT")
    print("=" * 70)
    print()
    
    if results['valid']:
        print("✅ VALIDATION PASSED")
    else:
        print("❌ VALIDATION FAILED")
    
    print()
    
    # Print errors
    if results['errors']:
        print("ERRORS:")
        print("-" * 70)
        for error in results['errors']:
            print(f"  ❌ {error}")
        print()
    
    # Print warnings
    if results['warnings']:
        print("WARNINGS:")
        print("-" * 70)
        for warning in results['warnings']:
            print(f"  ⚠️  {warning}")
        print()
    
    # Print info
    if results['info']:
        print("INFO:")
        print("-" * 70)
        for info in results['info']:
            print(f"  ℹ️  {info}")
        print()
    
    print("=" * 70)
    print(f"Total: {len(results['errors'])} errors, {len(results['warnings'])} warnings")
    print("=" * 70)
    
    return results['valid']


def main():
    """Main entry point."""
    # Parse arguments
    if len(sys.argv) > 1:
        skill_path = sys.argv[1]
    else:
        skill_path = None
    
    validator = SkillValidator(skill_path)
    results = validator.validate()
    
    # Print results
    valid = print_validation_results(results)
    
    # Exit with appropriate code
    # 0 = valid
    # 1 = invalid (errors)
    # 2 = warnings only
    if not valid:
        sys.exit(1)
    elif results['warnings']:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
