from agent import generate_project_spec
from scaffold import create_scaffold

def main():
    user_paragraph = input("Describe your project: ")
    spec = generate_project_spec(user_paragraph)

    print("\n--- Project Spec ---")
    print("Requirements:", spec["requirements"])
    print("Tech Stack:", spec["tech_stack"])
    print("Architecture:", spec["architecture"])
    print("Setup Instructions:", spec["setup_instructions"])

    create_scaffold(spec["scaffold"])
    print("\n✅ Project scaffold created in 'generated_project/'")

if __name__ == "__main__":
    main()