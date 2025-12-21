from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

def generate_handout():
    doc = SimpleDocTemplate("lesson2_handout.pdf", pagesize=A4,
                            rightMargin=20*mm, leftMargin=20*mm,
                            topMargin=20*mm, bottomMargin=20*mm)
    
    styles = getSampleStyleSheet()
    story = []

    # Title
    title_style = styles['Title']
    title_style.alignment = 0 # Left
    story.append(Paragraph("TOEFL Writing Workshop", title_style))
    story.append(Paragraph("Lesson 2: Sentence Variety & Logical Flow", styles['Heading2']))
    story.append(Spacer(1, 5*mm))
    
    # Metadata
    normal_style = styles['Normal']
    story.append(Paragraph("<b>Student:</b> George", normal_style))
    story.append(Paragraph("<b>Topic:</b> Independent Study vs Group Work", normal_style))
    story.append(Paragraph("<b>Core Argument:</b> While teamwork has its merits, independent study cultivates deeper cognitive engagement.", normal_style))
    story.append(Spacer(1, 10*mm))
    
    # Section Header
    story.append(Paragraph("I. Sentence-by-Sentence Analysis", styles['Heading3']))
    story.append(Spacer(1, 2*mm))

    # Data
    data = [
    ("01", "When faced with the choice between studying alone or in a group, opinions often vary.", "Grammar", "Uses 'When faced with' (Past Participle Phrase) instead of 'When people face'. 'Vary' is a strong verb choice."),
    ("02", "While some argue for group work, I personally believe that studying individually is far more effective.", "Logic", "Classic 'While A, B' structure showing critical thinking. 'Fosters' and 'Individually' are precise vocabulary."),
    ("03", "This approach not only minimizes unnecessary distractions but also facilitates a deeper level of cognitive engagement.", "Structure", "Uses 'Not only... but also...' parallelism. 'Cognitive engagement' is an excellent academic term."),
    ("04", "First and foremost, studying alone significantly enhances concentration.", "Focus", "Strong Topic Sentence clearly stating the main advantage (Concentration)."),
    ("05", "In a group setting, it is all too easy for academic discussions to devolve into casual conversations.", "Vocab", "'Devolve into' vividly describes the negative progression."),
    ("06", "For instance, last week, I attempted to collaborate with a partner on a project regarding the Chinese Civil War (1945-1949).", "Detail", "Specific historical event adds credibility."),
    ("07", "Instead of focusing on the strategic analysis, we ended up wasting valuable time gossiping about anecdotes.", "Structure", "'Instead of A, B' highlights the contrast. 'Anecdotes' replaces 'stories'."),
    ("08", "Realizing the inefficiency, I decided to work in a quiet environment.", "Grammar", "Participle phrase 'Realizing...' sets the context efficiently."),
    ("09", "Liberated from external disturbances, I clarified my research plan and executed it with much greater speed and precision.", "Vocab", "'Liberated from' (high-level adjective). 'Precision' implies accuracy."),
    ("10", "Furthermore, independent study is indispensable for tasks requiring deep critical thinking.", "Vocab", "'Indispensable' is a strong, definitive adjective."),
    ("11", "Unlike brainstorming sessions which benefit from divergent views, analyzing complex historical data demands a singular, uninterrupted focus.", "Logic", "Nuanced comparison distinguishing 'Brainstorming' (Group) vs 'Analysis' (Solo)."),
    ("12", "When I organized intricate timelines... working alone allowed me to annotate materials and synthesize information deeply...", "Key Phrase", "'Synthesize' means to combine parts into a whole - very academic."),
    ("13", "With the assistance of AI tools, I could build a solid knowledge framework efficiently.", "Modern", "Incorporates modern tools (AI) into the workflow."),
    ("14", "In conclusion, while teamwork has its place, the benefits of solitary study are undeniable.", "Conclusion", "Re-states opinion objectively ('Undeniable') while conceding teamwork has value."),
    ("15", "Therefore, I prefer to study alone to maximize my academic performance.", "Finality", "Clear, direct closing statement.")
    ]

    # Create Table Data
    table_data = []
    # Header
    table_data.append([Paragraph("<b>#</b>", normal_style), Paragraph("<b>Sentence & Analysis</b>", normal_style)])

    for num, sent, type_, content in data:
        # Cell 2 content: Sentence + Analysis Box
        cell_content = [
            Paragraph(f"<b>{sent}</b>", normal_style),
            Spacer(1, 2*mm),
            Paragraph(f"<font color='blue'>[{type_}]</font> {content}", normal_style)
        ]
        table_data.append([num, cell_content])

    # Table Style
    t = Table(table_data, colWidths=[10*mm, 160*mm])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    
    story.append(t)
    
    doc.build(story)
    print("PDF Generated Successfully")

if __name__ == "__main__":
    generate_handout()
