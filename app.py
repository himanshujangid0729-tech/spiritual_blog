from flask import Flask, render_template, abort

app = Flask(__name__)

# Topics and subtopics
topics = {
    "Bhagavad Gita Chapter Summary": {
        "Introduction": "Bhagavad Gita introduces the conversation between Krishna and Arjuna.",
        "Karma Yoga": "Karma Yoga is the path of selfless action, working without attachment to results."
    },
    "Bhagavad Gita":{
        
    },
    "Ramayan": {
        "Story of Lord Rama": "Lord Rama shows the path of dharma.",
        "Hanuman’s Devotion": "Hanuman’s devotion to Rama is an example for all."
    },
    "Lessons from Mahabharat":{
        
    },
    "Kartik Damodar Lila":{
        
    },
    "Ekadashi":{
        
    },
    "Radhashtami":{
        
    },
    "Janmashtami":{
        
    },
     "Cosmic Creation":{
        
    },
    "Lord Shiva":{
        
    },
    "Who is Devtas":{
        
    },
    "Special Tithies":{
        
    },
    "Jayanti":{
        
    },
    "Special lecture":{
        
    },
    "Articles":{
        
    },
    "Popular Vaishnav Songs":{
        
    },
    "Prabhupada Quotes":{
        
    },
    
}

# Homepage: show first topic/subtopic
@app.route("/")
def index():
    first_topic = list(topics.keys())[0]
    first_sub = list(topics[first_topic].keys())[0]
    content = topics[first_topic][first_sub]
    return render_template("index.html", topics=topics, main=first_topic, sub=first_sub, content=content)

# Blog page: specific topic/subtopic
@app.route("/topic/<main>/<sub>")
def blog(main, sub):
    main = main.replace("-", " ")
    sub = sub.replace("-", " ")
    if main not in topics or sub not in topics[main]:
        abort(404)
    content = topics[main][sub]
    return render_template("blog.html", topics=topics, main=main, sub=sub, content=content)

if __name__ == "__main__":
    app.run(debug=True)
