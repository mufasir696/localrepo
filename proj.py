# -----------------------------
# Mini CodeGPT: AI Coding Assistant
# -----------------------------

# OOP Classes
class CodeSnippet:
    def __init__(self, language, code_lines):
        self.language = language
        self.code_lines = code_lines  # list of code lines
        self.errors = []              # list of tuples: (line_no, error_msg)

class CodeGPT:
    def __init__(self):
        self.history = []  # store CodeSnippet objects

    # Template code generator for simple tasks
    def generate_code(self, language, task):
        templates = {
            "Python": {
                "sum_two_numbers": ["def sum_two_numbers(a, b):", "    return a + b"],
                "factorial": ["def factorial(n):", "    if n==0:", "        return 1", "    else:", "        return n*factorial(n-1)"]
            },
            "Java": {
                "sum_two_numbers": ["int sumTwoNumbers(int a, int b) {", "    return a + b;", "}"],
                "factorial": ["int factorial(int n) {", "    if(n==0) return 1;", "    else return n*factorial(n-1);", "}"]
            },
            "C++": {
                "sum_two_numbers": ["int sumTwoNumbers(int a, int b) {", "    return a + b;", "}"],
                "factorial": ["int factorial(int n) {", "    if(n==0) return 1;", "    else return n*factorial(n-1);", "}"]
            }
        }
        return templates.get(language, {}).get(task, ["# Task template not found"])

    # Simple rule-based error detection
    def check_errors(self, snippet):
        snippet.errors.clear()
        for i, line in enumerate(snippet.code_lines):
            line_no = i + 1
            if snippet.language == "Python":
                if line.strip().endswith("if") or line.strip().startswith("def") and not line.strip().endswith(":"):
                    snippet.errors.append((line_no, "Missing colon ':'"))
                if line.count("(") != line.count(")"):
                    snippet.errors.append((line_no, "Mismatched parentheses"))
            elif snippet.language in ["Java", "C++"]:
                if line.strip() and not line.strip().endswith(";") and not line.strip().endswith("{") and not line.strip().endswith("}"):
                    if not line.strip().startswith(("if", "else", "for", "while", "int", "return")):
                        snippet.errors.append((line_no, "Missing semicolon"))
        return snippet.errors

    # Suggest fix (basic)
    def suggest_fix(self, snippet):
        suggestions = []
        for line_no, error in snippet.errors:
            if "Missing colon" in error:
                suggestions.append(f"Line {line_no}: Add ':' at the end")
            elif "Mismatched parentheses" in error:
                suggestions.append(f"Line {line_no}: Check parentheses")
            elif "Missing semicolon" in error:
                suggestions.append(f"Line {line_no}: Add ';' at the end")
        return suggestions

# -----------------------------
# File Handling
# -----------------------------
def save_snippet(snippet):
    with open("code_history.txt", "a") as f:
        f.write(f"Language: {snippet.language}\n")
        f.write("Code:\n")
        for line in snippet.code_lines:
            f.write(line + "\n")
        f.write("Errors:\n")
        for err in snippet.errors:
            f.write(f"Line {err[0]}: {err[1]}\n")
        f.write("\n---\n\n")

# -----------------------------
# Recursive Menu
# -----------------------------
def main_menu(ai):
    print("\n=== Mini CodeGPT ===")
    print("1. Generate Code Template")
    print("2. Check Your Code for Errors")
    print("3. View History")
    print("4. Exit")
    choice = input("Choose option: ")

    if choice == '1':
        generate_code_menu(ai)
        main_menu(ai)
    elif choice == '2':
        check_code_menu(ai)
        main_menu(ai)
    elif choice == '3':
        view_history()
        main_menu(ai)
    elif choice == '4':
        print("Goodbye!")
    else:
        print("Invalid choice. Try again.")
        main_menu(ai)

# -----------------------------
# Submenus
# -----------------------------
def generate_code_menu(ai):
    language = input("Enter language (Python/Java/C++): ")
    task = input("Enter task (sum_two_numbers/factorial): ")
    code_lines = ai.generate_code(language, task)
    print("\nGenerated Code:")
    for line in code_lines:
        print(line)
    snippet = CodeSnippet(language, code_lines)
    ai.history.append(snippet)
    save_snippet(snippet)

def check_code_menu(ai):
    language = input("Enter language of your code (Python/Java/C++): ")
    print("Enter your code (type 'END' in a new line to finish):")
    code_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        code_lines.append(line)
    snippet = CodeSnippet(language, code_lines)
    ai.check_errors(snippet)
    suggestions = ai.suggest_fix(snippet)
    if snippet.errors:
        print("\nDetected Errors:")
        for err in snippet.errors:
            print(f"Line {err[0]}: {err[1]}")
        print("\nSuggestions:")
        for s in suggestions:
            print(s)
    else:
        print("No errors detected! ✅")
    ai.history.append(snippet)
    save_snippet(snippet)

def view_history():
    try:
        with open("code_history.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No history found.")

# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":
    ai = CodeGPT()
    main_menu(ai)
