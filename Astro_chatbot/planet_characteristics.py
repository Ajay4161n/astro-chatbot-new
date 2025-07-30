# planet_characteristics.py

def interpret_planets(planets):
    detailed_traits = {
        "Sun": {
            1: "strong self-image and leadership qualities",
            2: "focus on wealth and family values",
            3: "communication and sibling relationships are vital",
            4: "emotional foundation and home matters",
            5: "creativity, children, and fame",
            6: "conflict with enemies or health improvement",
            7: "emphasis on partnership and public image",
            8: "transformation through ego and power struggles",
            9: "spiritual pursuits and luck through authority",
            10: "career-oriented with ambition",
            11: "social circles, gains from leadership",
            12: "detachment from ego, spiritual isolation"
        },
        "Moon": {
            1: "emotional awareness and sensitivity",
            2: "emotions tied to possessions and family",
            3: "expressive and emotional communication",
            4: "deeply emotional about home and roots",
            5: "creative emotional expression",
            6: "mental stress or healing through routine",
            7: "emotional bonding in relationships",
            8: "emotional intensity and psychic abilities",
            9: "intuitive belief systems and travel",
            10: "emotional investment in career",
            11: "comfort through friendships",
            12: "need for solitude and spiritual connection"
        },
        "Mars": {
            1: "energetic and assertive personality",
            2: "aggression in speech or earning money",
            3: "courage in communication and travel",
            4: "agitated emotions or home conflicts",
            5: "passion in romance and creativity",
            6: "fighter of diseases, good for discipline",
            7: "aggression in partnerships",
            8: "risk-taking, sexual energy, sudden changes",
            9: "fighting for beliefs or father figure",
            10: "ambitious and active career goals",
            11: "competitive in social network",
            12: "hidden anger, spiritual warrior"
        },
        "Mercury": {
            1: "analytical mind and expressive personality",
            2: "clever with finance and speech",
            3: "gifted communicator and writer",
            4: "logical in emotional matters",
            5: "intelligent and witty in romance",
            6: "skillful in service and healing",
            7: "communicative partner",
            8: "research-oriented, deep thinker",
            9: "philosophical thinker",
            10: "intellect in profession",
            11: "networking skills",
            12: "secretive intellect, spiritual messenger"
        },
        "Jupiter": {
            1: "wise and morally guided personality",
            2: "wealth through knowledge",
            3: "expansion in communication",
            4: "spiritual home environment",
            5: "fortunate with children and creativity",
            6: "spiritual approach to service",
            7: "spouse is wise and spiritual",
            8: "deep transformation through belief",
            9: "teacher or guru-like personality",
            10: "expansion in profession",
            11: "benefits through community",
            12: "spiritual isolation, moksha seeker"
        },
        "Venus": {
            1: "charming and attractive personality",
            2: "love for wealth and beauty",
            3: "artistic in communication",
            4: "beauty in home life",
            5: "romantic and artistic nature",
            6: "conflicts in love or hidden beauty",
            7: "balanced and romantic partner",
            8: "hidden pleasures, secret affairs",
            9: "love for travel and higher learning",
            10: "artistic career or fame",
            11: "gains from love or art",
            12: "spiritual love, artistic in isolation"
        },
        "Saturn": {
            1: "serious and disciplined personality",
            2: "delayed wealth but long-term gains",
            3: "slow but structured communication",
            4: "strict home environment",
            5: "delayed children, strict creativity",
            6: "strong service karma, hard-working",
            7: "karmic relationships, delay in marriage",
            8: "transformation through struggle",
            9: "restrained beliefs, serious guru",
            10: "responsible and structured career",
            11: "disciplined gains and older friends",
            12: "painful isolation, spiritual tests"
        },
        "Rahu": {
            1: "obsessed with self-image",
            2: "desire for wealth and status",
            3: "innovative in communication",
            4: "strange home situations",
            5: "creative genius or illusion",
            6: "master of manipulation in competition",
            7: "obsession with relationships",
            8: "occult fascination, risky transformation",
            9: "foreign or unusual belief systems",
            10: "unconventional career rise",
            11: "weird friends, obsessive ambitions",
            12: "illusion in isolation, secret addictions"
        },
        "Ketu": {
            1: "spiritual disconnect with ego",
            2: "detachment from wealth or speech",
            3: "introverted speaker, detached sibling bond",
            4: "quiet and spiritual home",
            5: "lack of interest in romance",
            6: "spiritual healer, unconcerned with enemies",
            7: "detached spouse or karmic relationship",
            8: "spiritual transformation, intuitive powers",
            9: "inner guru, detachment from religion",
            10: "lack of career interest, inward focus",
            11: "no desire for gains or fame",
            12: "moksha-focused, high detachment"
        }
    }

    interpretations = []
    for planet, house in planets.items():
        desc = detailed_traits.get(planet, {}).get(house, "influential in an unusual way")
        interpretations.append(f"{planet} in House {house}: {desc}.")

    return interpretations
