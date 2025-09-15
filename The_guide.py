class Profile:
    def __init__(self, name, favorite_language="Python", hobby="Coding",
                 tech_stack=None, github_username=None, fun_fact=""):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack or []
        self.github_username = github_username
        self.fun_fact = fun_fact

    def __str__(self):
        return f"Hi, I'm {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}."

    def introduce(self):
        print(str(self))
        if self.fun_fact:
            print(f"Fun fact: {self.fun_fact}")

    def show_stack(self):
        if not self.tech_stack:
            print("No technologies listed yet.")
            return
        print("My tech stack includes:")
        print("\n".join(f"- {tech}" for tech in self.tech_stack))

    def github_link(self):
        return f"https://github.com/{self.github_username}" if self.github_username else "No GitHub username provided."


# Example usage
if __name__ == "__main__":
    my_profile = Profile(
        name="George",
        favorite_language="Python",
        hobby="Exploring OS installations",
        tech_stack=["Python", "Rufus", "GParted", "Git", "LaTeX"],
        github_username="Sirgeorgemunguchi",
        fun_fact="I once installed Ubuntu offline using just a USB stick! And i love to play football and watch movies."
    )

    my_profile.introduce()
    my_profile.show_stack()
    print("GitHub Profile:", my_profile.github_link())
