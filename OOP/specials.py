class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.director}!"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("Film silindi.")

m = Movie("Bodies", "Mustafa", 126)

print(m)
print(len(m))