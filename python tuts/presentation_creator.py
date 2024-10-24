# Correcting the add_paragraph method usage to properly add text to the text frame

# Create a presentation object
prs = Presentation()

# Title Slide
slide_title = prs.slides.add_slide(prs.slide_layouts[0])
title = slide_title.shapes.title
subtitle = slide_title.placeholders[1]
title.text = "PHP for Absolute Beginners"
subtitle.text = "Duration: 1 Hour | By [Your Name]"

# Part 1: Introduction to PHP
slide1 = prs.slides.add_slide(prs.slide_layouts[1])
title1 = slide1.shapes.title
title1.text = "Part 1: Introduction to PHP (5 minutes)"

content1 = slide1.shapes.placeholders[1].text_frame
content1.text = "English Explanation: What is PHP? How does it work with web servers?"
p = content1.add_paragraph()
p.text = "Why is it popular for web development?"
p = content1.add_paragraph()
p.text = "Hindi Explanation: PHP kya hai? Yeh web server ke sath kaise kaam karta hai?"
p = content1.add_paragraph()
p.text = "Web development ke liye yeh kyun famous hai?"

# Part 2: Setting up the Environment
slide2 = prs.slides.add_slide(prs.slide_layouts[1])
title2 = slide2.shapes.title
title2.text = "Part 2: Setting up the Environment (10 minutes)"

content2 = slide2.shapes.placeholders[1].text_frame
content2.text = "English: Downloading and installing XAMPP (Windows) or MAMP (macOS)"
p = content2.add_paragraph()
p.text = "Setting up a local server for running PHP scripts."
p = content2.add_paragraph()
p.text = "Hindi: XAMPP ya MAMP ko kaise install karein aur PHP scripts run karne ke liye local server kaise set karein."

# Part 3: Writing Your First PHP Script
slide3 = prs.slides.add_slide(prs.slide_layouts[1])
title3 = slide3.shapes.title
title3.text = "Part 3: Writing Your First PHP Script (5 minutes)"

content3 = slide3.shapes.placeholders[1].text_frame
content3.text = 'English: Writing a basic PHP script with the `echo` function to display "Hello, World!"'
p = content3.add_paragraph()
p.text = 'Hindi: Ek simple PHP script likhna jo `echo` function ka use karke "Hello, World!" display karta hai.'

# Part 4: PHP Variables and Data Types
slide4 = prs.slides.add_slide(prs.slide_layouts[1])
title4 = slide4.shapes.title
title4.text = "Part 4: PHP Variables and Data Types (10 minutes)"

content4 = slide4.shapes.placeholders[1].text_frame
content4.text = "English: Explanation of PHP variables (`$` symbol) and different data types (strings, integers, floats, etc.)"
p = content4.add_paragraph()
p.text = "Hindi: PHP variables aur unke alag-alag data types ka samajhna (string, integer, float, etc.)"

# Part 5: PHP Conditional Statements
slide5 = prs.slides.add_slide(prs.slide_layouts[1])
title5 = slide5.shapes.title
title5.text = "Part 5: PHP Conditional Statements (10 minutes)"

content5 = slide5.shapes.placeholders[1].text_frame
content5.text = "English: Introduction to `if`, `else`, `elseif`, and `switch` statements."
p = content5.add_paragraph()
p.text = "Hindi: `if`, `else`, `elseif`, aur `switch` statements ka introduction."

# Part 6: Loops in PHP
slide6 = prs.slides.add_slide(prs.slide_layouts[1])
title6 = slide6.shapes.title
title6.text = "Part 6: Loops in PHP (10 minutes)"

content6 = slide6.shapes.placeholders[1].text_frame
content6.text = "English: Understanding `for`, `while`, and `foreach` loops in PHP with examples."
p = content6.add_paragraph()
p.text = "Hindi: `for`, `while`, aur `foreach` loops ka use PHP me examples ke sath samajhna."

# Part 7: Arrays in PHP
slide7 = prs.slides.add_slide(prs.slide_layouts[1])
title7 = slide7.shapes.title
title7.text = "Part 7: Arrays in PHP (5 minutes)"

content7 = slide7.shapes.placeholders[1].text_frame
content7.text = "English: Introduction to arrays, how to create, access, and manipulate arrays."
p = content7.add_paragraph()
p.text = "Hindi: Arrays kya hote hain aur kaise banate aur manipulate karte hain."

# Part 8: PHP Functions
slide8 = prs.slides.add_slide(prs.slide_layouts[1])
title8 = slide8.shapes.title
title8.text = "Part 8: PHP Functions (5 minutes)"

content8 = slide8.shapes.placeholders[1].text_frame
content8.text = "English: Creating and calling functions in PHP."
p = content8.add_paragraph()
p.text = "Hindi: PHP me functions kaise banayein aur unhe kaise call karein."

# Save the presentation
pptx_file = "/mnt/data/PHP_for_Absolute_Beginners_Tutorial.pptx"
prs.save(pptx_file)

pptx_file
