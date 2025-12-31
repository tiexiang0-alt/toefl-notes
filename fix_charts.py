import re

file_path = 'article_2026_outlook.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new corrected function
new_function = r"""        function renderInlineWidgets() {
            
            // --- 22 VISUALIZATION DATA POINTS (Mapped to Topics) ---
            const dataWidgets = [
                // Topic 0: China's Economy
                {
                    topicIdx: 0, type: 'gauge', label: "China 2025 GDP Target", value: 5.0, max: 8, unit: '%',
                    desc: "Growth Target Met: Yes", color: '#27ae60'
                },
                {
                    topicIdx: 0, type: 'chart-line-area', id: 'pmiChart', title: "China PMI Inflection Point",
                    labels: ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    data: [49.5, 49.0, 49.3, 49.1, 49.8, 49.5, 49.4, 50.2], 
                    color: '#e67e22', desc: "Dec broke 8-month contraction (>50)"
                },

                // Topic 1: Warner Bros vs Paramount
                {
                    topicIdx: 1, type: 'chart-bar-grouped', id: 'warnerBids', title: "Hollywood Bidding War ($bn)",
                    labels: ['Valuation'],
                    datasets: [
                        { label: 'Netflix Offer', data: [83], backgroundColor: '#e74c3c' },
                        { label: 'Paramount Bid', data: [108], backgroundColor: '#3498db' }
                    ],
                    desc: "Board favors Netflix despite lower bid"
                },
                {
                    topicIdx: 1, type: 'timeline-milestone', title: "Warner/Netflix/Paramount Timeline",
                    events: [
                        { date: 'Day 0', text: 'Nintendo Deal Announced' },
                        { date: 'Day +3', text: 'Paramount Swoops In ($108bn)' },
                        { date: 'Next Week', text: 'Board Final Decision' }
                    ]
                },

                // Topic 2: Iran Protests
                {
                    topicIdx: 2, type: 'chart-line', id: 'rialChart', title: "Iran Rial vs USD (Plunge)",
                    labels: ['2023', '2024', '2025', 'Jan 2026'],
                    data: [42000, 50000, 65000, 95000], 
                    color: '#c0392b', desc: "Currency at historic low"
                },
                {
                    topicIdx: 2, type: 'thermometer', label: "Iran Inflation", value: 42, max: 60, unit: '%',
                    color: '#e74c3c', desc: "Hyper-inflation pressure"
                },

                // Topic 3: UN Budget Crisis
                {
                    topicIdx: 3, type: 'chart-doughnut', id: 'unBudget', title: "UN 2026 Budget Distribution",
                    labels: ['Approved ($3.45bn)', 'Cut (7%)'],
                    data: [93, 7],
                    colors: ['#3498db', '#bdc3c7'], desc: "Total slashed by $260m"
                },
                {
                    topicIdx: 3, type: 'chart-bar-horizontal', id: 'unArrears', title: "UN Funding Shortfall Contribution",
                    labels: ['USA Arrears', 'Rest of World'],
                    data: [1.4, 0.2], 
                    colors: ['#c0392b', '#95a5a6'], desc: "US owes 87% of deficit"
                },

                // Topic 4: Guinea Election
                {
                    topicIdx: 4, type: 'progress-circle', label: "Guinea Election share", value: 86,
                    color: '#27ae60', desc: "Gen. Doumbouya's disputed win"
                },

                // Topic 5: India Steel Tariffs
                {
                    topicIdx: 5, type: 'chart-step', id: 'steelTariff', title: "India Steel Tariff Step-Down",
                    labels: ['Year 1', 'Year 2', 'Year 3'],
                    data: [12, 11.5, 11],
                    color: '#f39c12', desc: "Excludes Stainless Steel"
                },
                {
                    topicIdx: 5, type: 'treemap-simple', title: "Steel Stocks Reaction",
                    items: [
                        { label: 'Tata Steel', change: '+5.2%', color: '#2ecc71' },
                        { label: 'JSW Steel', change: '+4.8%', color: '#2ecc71' },
                        { label: 'Small Caps', change: '+1.2%', color: '#27ae60' }
                    ]
                },

                // Topic 6: Warren Buffett Steps Down
                {
                    topicIdx: 6, type: 'timeline-long', title: "Buffett's 60-Year Reign",
                    start: '1965 (Textile Mill)', end: '2026 (Global Titan)',
                    desc: "longest tenure of S&P 500 CEO"
                },
                {
                    topicIdx: 6, type: 'org-chart', title: "Berkshire Succession",
                    top: "Warren Buffett (Chairman)",
                    child: "Greg Abel (CEO)",
                    desc: "Effective Jan 1st"
                },

                // Topic 7: Figure of the Day
                {
                    topicIdx: 7, type: 'heatmap-lite', title: "LA Fire Damage Density",
                    value: "High", location: "Los Angeles County", count: "16,000 Buildings",
                    color: '#e74c3c'
                },

                // Topic 8: Politics: Democrats Step Up
                {
                    topicIdx: 8, type: 'parliament-sim', title: "2026 House Prediction",
                    dems: 220, reps: 215, desc: "Dems likely to retake majority"
                },
                {
                    topicIdx: 8, type: 'card-vs', title: "2028 Dem Frontrunners",
                    left: { name: 'J.B. Pritzker', role: 'IL Governor', tag: 'Wealth/Establishment' },
                    right: { name: 'Gavin Newsom', role: 'CA Governor', tag: 'Media/Policy' }
                },

                // Topic 9: Mass Deportation Campaign
                {
                    topicIdx: 9, type: 'fishbone-text', title: "Deportation Drivers",
                    head: "Mass Deportation",
                    bones: ['Funding (Bill Act)', 'Labor Shortage Fear', 'Public Opinion Drop'],
                },
                {
                    topicIdx: 9, type: 'chart-line', id: 'trumpApproval', title: "Immigration Approval Rating",
                    labels: ['Inauguration', 'Year 1', 'Year 2'],
                    data: [48, 42, 35],
                    color: '#e74c3c', desc: "Steady decline since taking office"
                },

                // Topic 10: President & Supreme Court
                {
                    topicIdx: 10, type: 'scoreboard', title: "SCOTUS 2026 Scorecard",
                    wins: ['Trans Ban', 'Dept of Ed Gutting', 'Official Firings'],
                    losses: ['Birthright Citizenship', 'Tariff Legality'],
                    desc: "Trump Agenda: Mixed Bag"
                },
                {
                    topicIdx: 10, type: 'funnel-text', title: "Judicial Process",
                    stages: ['Shadow Docket (Emergency)', 'Oral Arguments', 'Merits Ruling (Final)'],
                    desc: "Major cases moving to final stage"
                },

                // Topic 11: America's Big Birthday
                {
                    topicIdx: 11, type: 'venn-text', title: "America 250 Celebrations",
                    left: "Nonparisan Commission", right: "Trump's Task Force", center: "Conflict",
                    desc: "Battle over historical narrative"
                },
                 {
                    topicIdx: 11, type: 'map-text', title: "Global Hotspots",
                    points: ['Beijing', 'Tehran', 'Washington', 'Conakry', 'Mumbai'],
                    desc: "Key locations in this report"
                }
            ];

            // --- RENDER LOOP ---
            dataWidgets.forEach((item, idx) => {
                // Find Inline Container
                const container = document.getElementById(`widgets-${item.topicIdx}`);
                if (!container) return;

                const card = document.createElement('div');
                card.className = 'glass-panel p-6 rounded-2xl flex flex-col justify-between hover:scale-[1.02] transition duration-300 border border-white/30 bg-white/40 shadow-sm group min-h-[220px]';
                
                // HEADER
                const headerHtml = item.label || item.title ? `
                    <div class="flex justify-between items-start mb-4 border-b border-black/5 pb-2">
                        <span class="text-xs font-bold uppercase tracking-wider text-news-dark/60">${item.label || item.title}</span>
                        <span class="material-symbols-rounded text-news-dark/20 text-lg">bar_chart</span>
                    </div>` : '';

                let uniqueContent = '';

                // --- WIDGET TYPES ---

                // 1. GAUGE / THERMOMETER (Simple Radial or Bar)
                if (item.type === 'gauge' || item.type === 'thermometer') {
                    const pct = (item.value / item.max) * 100;
                    const isGauge = item.type === 'gauge';
                    uniqueContent = `
                        <div class="flex-1 flex flex-col items-center justify-center relative">
                             ${isGauge 
                                ? `<div class="w-32 h-16 overflow-hidden relative">
                                     <div class="absolute w-32 h-32 rounded-full border-[12px] border-black/10 border-b-0"></div>
                                     <div class="absolute w-32 h-32 rounded-full border-[12px] border-transparent border-t-${item.color === '#27ae60' ? 'green-500' : 'red-500'} origin-bottom transition-all duration-1000" style="transform: rotate(${pct * 1.8}deg)"></div>
                                   </div>`
                                : `<div class="w-8 h-32 bg-black/10 rounded-full relative overflow-hidden ring-4 ring-white/50">
                                     <div class="absolute bottom-0 w-full bg-red-500 transition-all duration-1000" style="height: ${pct}%"></div>
                                   </div>`
                             }
                             <div class="mt-4 text-3xl font-serif font-bold text-news-dark">${item.value}${item.unit || ''}</div>
                        </div>
                    `;
                }

                // 2. CHARTS (Chart.js)
                else if (item.type.startsWith('chart-')) {
                    const canvasId = `viz-${idx}`;
                    uniqueContent = `<div class="relative h-48 w-full"><canvas id="${canvasId}"></canvas></div>`;
                    
                    setTimeout(() => {
                        const ctx = document.getElementById(canvasId).getContext('2d');
                        let config = {};
                        
                        if (item.type === 'chart-line-area' || item.type === 'chart-line' || item.type === 'chart-step') {
                            config = {
                                type: 'line',
                                data: { labels: item.labels, datasets: [{ 
                                    label: item.title, data: item.data, 
                                    borderColor: item.color, backgroundColor: item.color + '20', 
                                    fill: item.type === 'chart-line-area', stepped: item.type === 'chart-step', tension: 0.3 
                                }]},
                                options: { maintainAspectRatio: false, plugins: { legend: {display: false} }, scales: { x: {display:false}, y: {display: false} } }
                            };
                        } else if (item.type === 'chart-bar-grouped') {
                            config = {
                                type: 'bar',
                                data: { labels: item.labels, datasets: item.datasets },
                                options: { maintainAspectRatio: false, scales: { y: {beginAtZero: true} } }
                            };
                        } else if (item.type === 'chart-doughnut') {
                            config = {
                                type: 'doughnut',
                                data: { labels: item.labels, datasets: [{ data: item.data, backgroundColor: item.colors }] },
                                options: { maintainAspectRatio: false, plugins: { legend: { position: 'bottom', labels: { boxWidth: 10 } } } }
                            };
                        } else if (item.type === 'chart-bar-horizontal') {
                            config = {
                                type: 'bar',
                                data: { labels: item.labels, datasets: [{ data: item.data, backgroundColor: item.colors }] },
                                options: { indexAxis: 'y', maintainAspectRatio: false, plugins: { legend: {display: false} } }
                            };
                        }
                        new Chart(ctx, config);
                    }, 100);
                }

                // 3. SPECIAL WIDGETS (HTML/CSS)
                
                else if (item.type === 'timeline-milestone') {
                    uniqueContent = `<div class="space-y-4 relative pl-4 border-l-2 border-dashed border-news-dark/20">
                        ${item.events.map(e => `
                            <div class="relative">
                                <div class="absolute -left-[21px] w-3 h-3 bg-news-dark rounded-full ring-4 ring-white"></div>
                                <div class="text-xs font-bold text-news-accent">${e.date}</div>
                                <div class="text-sm font-medium text-news-dark">${e.text}</div>
                            </div>
                        `).join('')}
                    </div>`;
                }
                
                else if (item.type === 'treemap-simple') {
                    uniqueContent = `<div class="grid grid-cols-2 gap-2 h-full">
                        ${item.items.map((t, i) => `
                            <div class="${i === 0 ? 'col-span-2' : ''} bg-green-100 rounded p-2 flex flex-col justify-center items-center border border-green-200">
                                <div class="font-bold text-green-800">${t.label}</div>
                                <div class="text-xs text-green-600">${t.change}</div>
                            </div>
                        `).join('')}
                    </div>`;
                }

                else if (item.type === 'progress-circle') {
                    uniqueContent = `
                        <div class="flex items-center justify-center py-4">
                            <div class="relative w-32 h-32 rounded-full border-8 border-gray-200 flex items-center justify-center">
                                <div class="text-3xl font-bold text-news-dark">${item.value}%</div>
                                <svg class="absolute inset-0 w-full h-full -rotate-90"><circle cx="64" cy="64" r="58" stroke="${item.color}" stroke-width="8" fill="none" class="stroke-[8] dash-array-100" style="stroke-dasharray: 365; stroke-dashoffset: ${365 - (365 * item.value/100)}"></circle></svg>
                            </div>
                        </div>
                    `;
                }

                else if (item.type === 'parliament-sim') {
                    uniqueContent = `
                        <div class="flex flex-col items-center">
                            <div class="flex gap-1 items-end h-24 mb-2">
                                <div class="w-16 bg-blue-600 rounded-t-lg h-full flex items-center justify-center text-white font-bold">Dems<br>${item.dems}</div>
                                <div class="w-1 bg-black/10 h-24"></div>
                                <div class="w-16 bg-red-600 rounded-t-lg h-[95%] flex items-center justify-center text-white font-bold opacity-60">Reps<br>${item.reps}</div>
                            </div>
                            <div class="text-center text-sm font-bold text-blue-600">Majority Flip</div>
                        </div>
                    `;
                }

                else if (item.type === 'card-vs') {
                    uniqueContent = `
                        <div class="flex justify-between items-center h-full">
                            <div class="text-center w-1/2 pr-2 border-r border-black/10">
                                <div class="text-2xl">🦁</div>
                                <div class="font-bold text-news-dark text-sm">${item.left.name}</div>
                                <div class="text-[10px] text-gray-500">${item.left.tag}</div>
                            </div>
                            <div class="text-center w-1/2 pl-2">
                                <div class="text-2xl">🐻</div>
                                <div class="font-bold text-news-dark text-sm">${item.right.name}</div>
                                <div class="text-[10px] text-gray-500">${item.right.tag}</div>
                            </div>
                        </div>
                    `;
                }

                else if (item.type === 'scoreboard') {
                    uniqueContent = `
                        <div class="grid grid-cols-2 gap-4 h-full">
                            <div class="bg-green-50 rounded p-3 border border-green-100">
                                <div class="text-xs font-bold text-green-700 mb-2 uppercase">Wins</div>
                                <ul class="text-[10px] list-disc list-inside text-green-900 space-y-1">
                                    ${item.wins.map(w => `<li>${w}</li>`).join('')}
                                </ul>
                            </div>
                             <div class="bg-red-50 rounded p-3 border border-red-100">
                                <div class="text-xs font-bold text-red-700 mb-2 uppercase">Losses</div>
                                <ul class="text-[10px] list-disc list-inside text-red-900 space-y-1">
                                    ${item.losses.map(w => `<li>${w}</li>`).join('')}
                                </ul>
                            </div>
                        </div>
                    `;
                }

                else if (item.type === 'funnel-text') {
                    uniqueContent = `
                        <div class="flex flex-col items-center space-y-1 w-full opacity-80">
                            ${item.stages.map((s, i) => `
                                <div class="bg-news-dark text-white text-xs py-1 px-4 text-center rounded shadow-sm" style="width: ${100 - (i*25)}%">${s}</div>
                            `).join('')}
                            <div class="text-center mt-2 text-xs">⬇️ Process</div>
                        </div>
                    `;
                }

                else if (item.type === 'fishbone-text') {
                    uniqueContent = `
                        <div class="relative flex items-center justify-between h-20 border-b-2 border-news-dark">
                             <div class="absolute right-0 text-xl font-bold bg-white px-2 border border-black z-10">${item.head}</div>
                             <div class="flex-1 flex justify-around items-end h-full pb-1">
                                ${item.bones.map(b => `<div class="text-[10px] text-center w-16 -rotate-45 mb-4 border-l border-black/20 pl-1">${b}</div>`).join('')}
                             </div>
                        </div>
                    `;
                }

                else if (item.type === 'timeline-long' || item.type === 'org-chart' || item.type === 'venn-text' || item.type === 'heatmap-lite' || item.type === 'map-text') {
                     uniqueContent = `
                        <div class="flex items-center justify-center h-full text-center flex-col">
                            <span class="material-symbols-rounded text-4xl text-news-accent/20 mb-2">dashboard</span>
                            <div class="font-bold text-news-dark">${item.title || item.label}</div>
                            <div class="text-xs text-news-dark/60 mt-1 max-w-[80%]">${item.desc}</div>
                            ${item.type === 'map-text' ? '<div class="text-[10px] mt-2 text-blue-600">📍 Multiple Locations</div>' : ''}
                        </div>
                     `;
                }

                card.innerHTML = headerHtml + uniqueContent + (item.desc ? `<div class="text-[10px] text-news-dark/50 font-medium border-t border-black/5 pt-2 mt-auto w-full text-right italic">${item.desc}</div>` : '');
                dashboard.appendChild(card);
            });
        }"""

# Use Regex to replace the function efficiently
# We target the function start and end. The content from view_file lines 1282 to 1622 shows it covers the whole function.
# We will construct a regex that matches `function renderDataDashboard` until the end of the `dataWidgets` and the loop.
# But matching brace counting is hard with regex.
# Instead, since we know it's at the end of the script tag, we can match from `function renderDataDashboard() {` up to `// Init`.

# Start pattern
pattern = r"function renderDataDashboard\(\) \{[\s\S]*?\}\s*(?=\/\/\s*Init)"
# Note: The `[\s\S]*?` is non-greedy, so it might stop too simple. 
# But `// Init` is right after.

replacement = new_function + "\n\n        "

new_content = re.sub(pattern, replacement, content)

# Also check if it actually replaced
if new_content == content:
    print("Error: Could not match the renderDataDashboard block.")
    # Fallback: try to find the start and just truncate-replace if needed, but let's try the regex first.
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success: Replaced renderDataDashboard with renderInlineWidgets.")
