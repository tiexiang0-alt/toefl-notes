import asyncio
import os
import edge_tts

# Sentences to generate audio for
sentences = [
    # Intro
    ("In the rapidly evolving landscape of 2026, web design has moved beyond simple aesthetics to focus on Human-Centric Digital Spaces.", "intro_1"),
    ("Modern web design ideas now emphasize a balance between AI-driven efficiency and authentic, tactile human expression.", "intro_2"),
    
    # Trending Concepts
    ("The current year is defined by a Warm Minimalism and the Human Layer in digital interfaces.", "trend_intro"),
    ("Tactile Maximalism: After years of flat design, we are seeing a more is more approach using rich textures, layered visuals, and sculptural 3D typography to create a sense of depth you can almost touch.", "trend_1"),
    ("Nature Distilled: Designers are moving toward organic shapes and muted, earthy palettes like the Pantone 2026 Color of the Year: Cloud Dancer.", "trend_2"),
    ("Agentic Web Experiences: Websites are no longer just static pages; they act as agents.", "trend_3a"),
    ("Using AI, they listen, watch, and respond to user needs in real-time, creating a conversational and highly personalized journey.", "trend_3b"),
    ("Kinetic Typography: Fonts are no longer sitting still.", "trend_4a"),
    ("Variable fonts now shift in weight, stretch, or react to your scroll and mouse movement, making the text itself part of the interface’s motion.", "trend_4b"),
    
    # Core Learning Pillars
    ("If you are studying web design today, these are the essential skills for 2026.", "pillars_intro"),
    ("AI Collaboration: Moving from simple prompts to using AI as a creative co-designer for layout optimization and accessibility audits.", "pillar_1"),
    ("Micro-Interactions: Focusing on Micro-delights—subtle button bounces or tactile toggles that provide instant, satisfying feedback.", "pillar_2"),
    ("Inclusive Design: Moving accessibility from a checklist to a creative default, ensuring high contrast and screen-reader compatibility from day one.", "pillar_3"),
    ("Performance-First: Optimizing for speed as a design constraint.", "pillar_4a"),
    ("Lightweight 3D and SVG-powered masks are used to keep sites fast but beautiful.", "pillar_4b"),

    # Toolkit
    ("Professional Toolkit for 2026.", "toolkit_title"),
    ("Figma remains the industry standard, but it's now heavily integrated with AI for rapid wireframing.", "toolkit_1"),
    ("Framer and Webflow are dominant for designers who want to build high-fidelity interactive sites without a deep coding background.", "toolkit_2"),
    ("Vibe Coding is a new trend where designers use AI to bridge the gap between a design vibe and functional code.", "toolkit_3"),

    # Inspiration
    ("To keep your ideas fresh, the top-rated galleries this year are Siteinspire, Landing Love, and Commerce Cream.", "inspiration_1")
]

OUTPUT_DIR = "audio/design_2026"
VOICE = "en-US-AndrewNeural"  # Professional, clear male voice

async def generate_audio():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    print(f"Generating {len(sentences)} audio files...")
    
    for text, filename in sentences:
        output_path = os.path.join(OUTPUT_DIR, f"{filename}.mp3")
        if os.path.exists(output_path):
            print(f"Skipping existing: {filename}")
            continue
            
        print(f"Generating: {filename}...")
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(output_path)
    
    print("All audio generation complete!")

if __name__ == "__main__":
    asyncio.run(generate_audio())
