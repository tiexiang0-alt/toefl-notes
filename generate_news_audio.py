import asyncio
import os
import edge_tts

# Full Article Data
articleSections = [
    {
        "topic": "China's Economy",
        "sentences": [
            ("China’s leader, Xi Jinping, said the economy would meet its growth target in 2025, with GDP expanding by around 5%.", "china_0_0"),
            ("Growth in exports buoyed the economy this year, though slowing investment and a property crisis dampened sentiment.", "china_0_1"),
            ("Meanwhile China’s official manufacturing purchasing managers’ index showed that factory activity increased unexpectedly in December, ending eight consecutive months of contraction.", "china_0_2")
        ]
    },
    {
        "topic": "Warner Bros vs Paramount",
        "sentences": [
            ("Warner Bros Discovery plans to reject its rival Paramount’s bid of $108bn to purchase the Hollywood studio.", "warner_1_0"),
            ("According to reports, Warner’s board still considers the $83bn offer from Netflix to be superior.", "warner_1_1"),
            ("Paramount had swooped in with its bid just days after Warner and Netflix had announced their deal.", "warner_1_2"),
            ("No final decision has been made yet, but Warner’s board is expected to meet next week.", "warner_1_3")
        ]
    },
    {
        "topic": "Iran Protests",
        "sentences": [
            ("Iran appointed a new central bank governor and announced a public holiday as anger over living standards prompted the largest anti-government demonstrations in years.", "iran_2_0"),
            ("The protests, which began on Sunday, have been fuelled by the country’s ailing economy.", "iran_2_1"),
            ("Iran’s currency, the rial, has plunged to record lows against the dollar and the annual inflation rate has risen above 40%.", "iran_2_2")
        ]
    },
    {
        "topic": "UN Budget Crisis",
        "sentences": [
            ("The United Nations slashed its budget for 2026 by 7%, to $3.45bn, and cut 2,900 jobs.", "un_3_0"),
            ("The organisation is grappling with a funding shortfall of nearly $1.6bn driven primarily by America, which owes more than $1.4bn in arrears.", "un_3_1"),
            ("The Trump administration has accused the UN of wasting taxpayer dollars.", "un_3_2")
        ]
    },
    {
        "topic": "Guinea Election",
        "sentences": [
            ("In Guinea, General Mamady Doumbouya won a presidential election that was marred by accusations of manipulation.", "guinea_4_0"),
            ("Provisional data published by the country’s election commission suggested General Doumbouya secured more than 86% of the vote; some opposition candidates were barred from running.", "guinea_4_1"),
            ("The junta leader seized power in a coup four years ago.", "guinea_4_2"),
            ("The election victory gives him a seven-year presidential term.", "guinea_4_3")
        ]
    },
    {
        "topic": "India Steel Tariffs",
        "sentences": [
            ("India extended a tariff on steel imports for three years as it tries to protect its producers from international oversupply, particularly from China.", "india_5_0"),
            ("The tariff rate will start at 12% before gradually decreasing to 11% over the three-year period.", "india_5_1"),
            ("Certain products, such as stainless steel, are exempt.", "india_5_2"),
            ("Shares in Indian steelmakers, including Tata Steel and JSW Steel, rallied on the news.", "india_5_3")
        ]
    },
    {
        "topic": "Warren Buffett Steps Down",
        "sentences": [
            ("Warren Buffett steps down as chief executive of Berkshire Hathaway, America’s ninth-most-valuable company, on Wednesday, ending his 60-year tenure at the helm.", "buffett_6_0"),
            ("Mr Buffett, who is 95, will remain chairman of Berkshire’s board.", "buffett_6_1"),
            ("Greg Abel, who is currently vice chair of non-insurance operations, will succeed him on January 1st.", "buffett_6_2")
        ]
    },
    {
        "topic": "Figure of the Day",
        "sentences": [
            ("Figure of the day: 16,000, the approximate number of buildings destroyed in the fires that tore across Los Angeles County nearly a year ago.", "figure_7_0")
        ]
    },
    {
        "topic": "Politics: Democrats Step Up",
        "sentences": [
            ("Until January 2nd we are looking ahead to next year’s big stories.", "dems_8_0"),
            ("Today, what will shape American politics?", "dems_8_1"),
            ("Donald Trump’s return to the presidency left Democrats in disarray.", "dems_8_2"),
            ("They lacked leadership and direction.", "dems_8_3"),
            ("Still, the party notched some impressive wins in state elections in November.", "dems_8_4"),
            ("And in 2026 its fight back could gain strength.", "dems_8_5"),
            ("In the midterm elections, Democrats will probably retake the House of Representatives.", "dems_8_6"),
            ("That would grant the Democrats subpoena power and the ability to go on the offensive.", "dems_8_7"),
            ("It would end Republicans’ lock on Congress and could set the stage for Mr Trump’s third impeachment.", "dems_8_8"),
            ("A welcome turn of events for the Democrats, then.", "dems_8_9"),
            ("But the out-of-power party usually gains in the midterms.", "dems_8_10"),
            ("Democrats’ longer-term fortunes will depend on who becomes their standard-bearer and eventual candidate in the 2028 presidential contest.", "dems_8_11"),
            ("Potential frontrunners include governors such as J.B. Pritzker in Illinois or Gavin Newsom in California.", "dems_8_12"),
            ("To succeed, the party will need to work out why voters still trust Republicans more on some of the most salient issues, including crime, immigration and the economy.", "dems_8_13")
        ]
    },
    {
        "topic": "Mass Deportation Campaign",
        "sentences": [
            ("Mass deportation was never going to be achieved in one year.", "deport_9_0"),
            ("The money and manpower required to round up thousands, let alone millions, of illegal immigrants would take time to secure.", "deport_9_1"),
            ("But Donald Trump’s first year in office has laid the groundwork.", "deport_9_2"),
            ("And in 2026 a dollop of cash from the One Big Beautiful Bill Act will fund more immigration agents, detention centres and surveillance technology.", "deport_9_3"),
            ("That means the deportation campaign will probably accelerate.", "deport_9_4"),
            ("But two factors could yet convince the president to ease up.", "deport_9_5"),
            ("First is potential pressure from businesses.", "deport_9_6"),
            ("Bosses in industries such as farming or tourism fear a labour shock.", "deport_9_7"),
            ("Second is public opinion.", "deport_9_8"),
            ("Approval for Mr Trump’s handling of immigration has plunged since he took office.", "deport_9_9"),
            ("Americans favour deporting criminals, but do not like to see masked agents shoving people into unmarked vans.", "deport_9_10"),
            ("Republicans up for re-election in November’s midterm elections might campaign less relentlessly for deportations than before.", "deport_9_11")
        ]
    },
    {
        "topic": "President & Supreme Court",
        "sentences": [
            ("Since Donald Trump returned to office, the Supreme Court has largely—with the significant exceptions of a National Guard deployment and a deportation case—blessed his agenda.", "court_10_0"),
            ("It has let him ban transgender soldiers from the armed forces, gut the Department of Education and rescind protections for more than 1m migrants.", "court_10_1"),
            ("But these judgments have come on the court’s “emergency” or “shadow” docket that produces interim rulings.", "court_10_2"),
            ("Several weighty questions are returning as slower-moving “merits” cases, which result in a final judgment.", "court_10_3"),
            ("When the court issues rulings in 2026, the president will find reasons to cheer—and a few to jeer.", "court_10_4"),
            ("His biggest wins could include the court formally blessing many of his attempts to sack government officials and employees.", "court_10_5"),
            ("As for the losses, the court will probably uphold the 14th Amendment’s guarantee of birthright citizenship, which Mr Trump tried to rescind in an executive order.", "court_10_6"),
            ("Meanwhile a ruling on his tariffs is expected in early 2026: a majority of justices expressed scepticism about their legality in oral arguments in November.", "court_10_7")
        ]
    },
    {
        "topic": "America's Big Birthday",
        "sentences": [
            ("In July America will celebrate its 250th birthday.", "bday_11_0"),
            ("The coming year will feature parades, fireworks and, curiously, an Ultimate Fighting Championship bout at the White House.", "bday_11_1"),
            ("The celebrations will be a sign of America’s political divisions.", "bday_11_2"),
            ("Two rival commissions are planning events.", "bday_11_3"),
            ("The “America250 Commission” was created by Congress in 2016 and aspires to a nonpartisan representation of the American story.", "bday_11_4"),
            ("“Task Force 250” was established by Donald Trump to “honour the history of our great nation”.", "bday_11_5"),
            ("The past has become a partisan battleground.", "bday_11_6"),
            ("To Mr Trump, it is the left that struck first, toppling statues of historical figures such as Confederate generals.", "bday_11_7"),
            ("In March he signed an executive order that complained of a “concerted” effort to “rewrite” America’s history to foster “a sense of national shame”.", "bday_11_8"),
            ("It called on officials to audit how the American story is told at federal historical sites and museums.", "bday_11_9"),
            ("Big anniversaries once provided moments of unity.", "bday_11_10"),
            ("Now that looks less likely.", "bday_11_11")
        ]
    }
]

OUTPUT_DIR = "audio/news_2026"
VOICE = "en-US-AndrewNeural" # Professional News Anchor style

async def generate_audio():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    print(f"Starting audio generation...")
    
    for section in articleSections:
        for text, filename in section["sentences"]:
            output_path = os.path.join(OUTPUT_DIR, f"{filename}.mp3")
            if os.path.exists(output_path):
                # print(f"Skipping existing: {filename}")
                continue
            
            print(f"Generating: {filename}...")
            try:
                communicate = edge_tts.Communicate(text, VOICE)
                await communicate.save(output_path)
            except Exception as e:
                print(f"Error generating {filename}: {e}")

    print("All audio generation complete!")

if __name__ == "__main__":
    asyncio.run(generate_audio())
