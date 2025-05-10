from ebooklib import epub

# Read the extracted text from file
with open("Java_Ultimate_Interview_Guide_Text.txt", "r", encoding="utf-8") as f:
    full_text = f.read()

# Create a new EPUB book
book = epub.EpubBook()
book.set_title("Java Ultimate Interview Guide")
book.set_language("en")
book.add_author("OpenAI GPT-4")

# Create a single chapter with all the content
chapter = epub.EpubHtml(title="Full Guide", file_name="chapter1.xhtml", lang="en")
chapter.set_content(f"<h1>Java Ultimate Interview Guide</h1><pre>{full_text}</pre>")

# Add the chapter and finalize
book.add_item(chapter)
book.spine = ["nav", chapter]
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# Write the EPUB to disk
epub.write_epub("Java_Ultimate_Interview_Guide.epub", book)
print("✅ EPUB file created successfully.")
