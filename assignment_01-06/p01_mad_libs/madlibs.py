import random
import time
import sys

def slow_print(text, delay=0.03):
    """Print text with a slight delay between characters for a more engaging effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_input(prompt):
    """Get user input with colorful prompts."""
    return input(f"\033[1;36m{prompt}\033[0m ")

def generate_madlib():
    """Generate a funny Mad Lib story based on user inputs."""
    
    # List of story templates
    stories = [
        {
            "title": "A Day at the Zoo",
            "template": """
Last week, I went to the zoo with my {adjective1} friend. We saw a(n) {adjective2} 
{animal} jumping up and down in its tree. It {verb_past1} through the large tunnel 
that led to its {adjective3} {noun1}. I got some peanuts and passed them through 
the cage to a gigantic gray {animal2} towering above my head. Feeding that animal 
made me {emotion}. The zookeeper told me that the {animal2} could {verb1} up to 
{number} {noun_plural} each day! Next time, I'll remember to bring my {adjective4} 
{noun2} so I can {verb2} as well!
            """,
            "prompts": {
                "adjective1": "adjective",
                "adjective2": "adjective",
                "animal": "animal",
                "verb_past1": "past tense verb",
                "adjective3": "adjective",
                "noun1": "noun",
                "animal2": "another animal",
                "emotion": "emotion",
                "verb1": "verb",
                "number": "number",
                "noun_plural": "plural noun",
                "adjective4": "adjective",
                "noun2": "noun",
                "verb2": "verb"
            }
        },
        {
            "title": "Space Adventure",
            "template": """
Captain's log, Stardate {number1}: We have encountered a(n) {adjective1} anomaly in the 
{adjective2} sector. My {job_title} officer, {silly_name}, suggested we {verb1} the ship's 
{noun1} to investigate. As we approached, a fleet of {adjective3} alien vessels 
{verb_past1} toward us. Their leader, who called himself the Grand {noun2}, demanded we 
surrender our cargo of {plural_noun1}. I responded by ordering my crew to {verb2} 
immediately! The aliens were so {emotion} that they {verb_past2} away at {adverb} speed. 
Now we're celebrating with a glass of {liquid} and {number2} pieces of {food}.
            """,
            "prompts": {
                "number1": "number",
                "adjective1": "adjective",
                "adjective2": "adjective",
                "job_title": "job title",
                "silly_name": "silly name",
                "verb1": "verb",
                "noun1": "noun",
                "adjective3": "adjective",
                "verb_past1": "past tense verb",
                "noun2": "noun",
                "plural_noun1": "plural noun",
                "verb2": "verb",
                "emotion": "emotion",
                "verb_past2": "past tense verb",
                "adverb": "adverb",
                "liquid": "liquid",
                "number2": "number",
                "food": "food"
            }
        },
        {
            "title": "The Magical Kitchen Disaster",
            "template": """
Today I tried to cook a(n) {adjective1} meal for my family. I started by {verb_ing1} 
{number1} {plural_noun1} into a large {container}. The recipe said to add {liquid}, but 
I accidentally used {silly_liquid} instead! As the mixture began to {verb1}, I noticed it 
turned {color} and smelled like {smelly_thing}. My {family_member} walked into the kitchen 
and {verb_past1} in shock! The concoction suddenly {verb_past2} and splattered all over the 
{room_item}. We had to {verb2} for {number2} hours to clean up the mess. Next time, I'll 
just order {fast_food_restaurant} instead!
            """,
            "prompts": {
                "adjective1": "adjective",
                "verb_ing1": "verb ending in -ing",
                "number1": "number",
                "plural_noun1": "plural noun",
                "container": "container",
                "liquid": "liquid",
                "silly_liquid": "silly liquid",
                "verb1": "verb",
                "color": "color",
                "smelly_thing": "something smelly",
                "family_member": "family member",
                "verb_past1": "past tense verb",
                "verb_past2": "past tense verb",
                "room_item": "item in a room",
                "verb2": "verb",
                "number2": "number",
                "fast_food_restaurant": "fast food restaurant"
            }
        }
    ]
    
    # Select a random story
    story = random.choice(stories)
    
    slow_print(f"\n\033[1;33m=== {story['title']} ===\033[0m")
    slow_print("\033[1;32mLet's create a funny Mad Lib! I'll ask for some words, then create a hilarious story with them.\033[0m")
    
    # Collect words from user
    words = {}
    for placeholder, prompt in story["prompts"].items():
        words[placeholder] = get_input(f"Enter a {prompt}:")
    
    # Format the template with the collected words
    mad_lib = story["template"]
    for placeholder, word in words.items():
        mad_lib = mad_lib.replace("{" + placeholder + "}", word)
    
    # Display the result with some formatting
    slow_print("\n\033[1;35m=== Your Hilarious Mad Lib Story ===\033[0m")
    time.sleep(1)
    slow_print(mad_lib.strip())
    
    return story["title"]

def main():
    """Main function to run the Mad Lib generator."""
    slow_print("\033[1;33m===== FUNNY STORY MAD LIB GENERATOR =====\033[0m")
    slow_print("\033[1;32mWelcome to the Mad Lib generator! Let's create some hilarious stories together!\033[0m")
    
    play_again = True
    completed_stories = []
    
    while play_again:
        title = generate_madlib()
        completed_stories.append(title)
        
        # Ask if user wants to play again
        response = get_input("\nWould you like to create another Mad Lib? (yes/no):").lower()
        play_again = response in ["yes", "y", "sure", "yeah"]
    
    # Show summary
    if completed_stories:
        slow_print("\n\033[1;33m=== Stories You Created ===\033[0m")
        for i, title in enumerate(completed_stories, 1):
            slow_print(f"{i}. {title}")
    
    slow_print("\n\033[1;32mThanks for playing! Come back soon for more Mad Lib fun!\033[0m")

if __name__ == "__main__":
    main()