# Andre Pereira
# Chapter 5
project_ideas = {
    'games': [
        'Text-based adventure RPG with a combat and inventory system',
        'A command-line version of Tic-Tac-Toe or Connect Four'
    ],
    'datasets': [
        'Analyze a CSV file of local weather trends over the last decade',
        'Track personal daily habits and visualize completion rates'
    ],
    'web_applications': [
        'Personal portfolio and blog website using Flask',
        'A flashcard study app for learning Python terminology'
    ]
}

# Function to display all current project ideas
def display_ideas(ideas):
    print("\n" + "="*30)
    print("      MY PYTHON PROJECT IDEAS")
    print("="*30)
    for category, list_of_ideas in ideas.items():
        print(f"\n📁 Category: {category.upper()}")
        for index, idea in enumerate(list_of_ideas, 1):
            print(f"   {index}. {idea}")
    print("\n" + "="*30)

# Display the initial list
display_ideas(project_ideas)

# Allow you to add a new idea interactively
print("\nWould you like to record a new project idea?")
add_choice = input("Enter 'yes' or 'no': ").strip().lower()

if add_choice == 'yes':
    print("\nAvailable categories: games, datasets, web_applications")
    category = input("Choose a category: ").strip().lower()
    
    if category in project_ideas:
        new_idea = input("Describe your project idea: ").strip()
        project_ideas[category].append(new_idea)
        print("\nSuccess! Here is your updated idea list:")
        display_ideas(project_ideas)
    else:
        print("That category doesn't exist, but keep brainstorming!")

print("\nKeep building and coding! 🚀")