"""Martial arts skills: discipline tags for the martial-arts pack (v2) and
the Indian martial arts pack. Solo practice only: stances, footwork,
shadow drills and conditioning. Partner and weapon work need a teacher.
"""

from authored import T, ex, step, MA_SAFE

STICK_SAFE = T("Use a light bamboo or PVC stick with clear space all around. Start slowly; never practise near people or pets.",
               "हल्की बाँस या PVC की छड़ी लें, चारों ओर जगह खाली रखें। धीरे शुरू करें; लोगों या पालतू जानवरों के पास कभी अभ्यास न करें।")
COND_SAFE = T("Build reps gradually and keep your back neutral. Stop if a joint hurts.",
              "गिनती धीरे-धीरे बढ़ाएँ और पीठ सीधी रखें। किसी जोड़ में दर्द हो तो रुकें।")


def sk(discipline, kind, *args, **kw):
    e = ex(*args, **kw)
    e["discipline"] = discipline
    e["kind"] = kind
    return e


# Tags for the original martial-arts exercises: id -> (discipline, kind)
TAGS = {
    "box_stance": ("boxing", "stance"), "box_jab_cross": ("boxing", "technique"),
    "box_hook": ("boxing", "technique"), "box_uppercut": ("boxing", "technique"),
    "mt_knee": ("muay_thai", "technique"),
    "karate_oi_zuki": ("karate", "technique"), "karate_age_uke": ("karate", "technique"),
    "karate_mae_geri": ("karate", "technique"),
    "kf_horse_stance": ("kung_fu", "stance"), "kf_horse_punch": ("kung_fu", "drill"),
    "kf_bow_stance": ("kung_fu", "stance"), "kf_crane": ("kung_fu", "stance"),
}
PROGRAM_TAGS = {"boxing_basics": "boxing", "karate_kihon": "karate", "kung_fu_stances": "kung_fu"}

WORLD_EXTRA = [
    sk("muay_thai", "technique", "mt_elbow", "martialArts", "elbow_strike", T("Elbow strike", "कोहनी का प्रहार"),
       T("A short-range strike that turns the whole body.", "कम दूरी का प्रहार जिसमें पूरा शरीर घूमता है।"),
       ["From guard, raise the elbow to shoulder height.", "Turn your hips and shoulders together.",
        "Swing the elbow across in a short arc.", "Return to guard."],
       ["गार्ड से कोहनी कंधे तक उठाएँ।", "कूल्हे और कंधे साथ घुमाएँ।", "कोहनी को छोटे घेरे में आर-पार घुमाएँ।", "गार्ड में लौटें।"],
       T("10 each side", "हर तरफ़ 10"), MA_SAFE),
    sk("muay_thai", "technique", "mt_teep", "martialArts", "front_kick", T("Push kick (Teep)", "पुश किक (टीप)"),
       T("Muay Thai's jab with the leg: keeps distance.", "पैर से मुए थाई का जैब: दूरी बनाए रखता है।"),
       ["Lift the knee in front of you.", "Push the foot straight out with the hip behind it.",
        "Pull the leg back and set it down in stance.", "Switch legs."],
       ["घुटना सामने उठाएँ।", "कूल्हे के ज़ोर से पैर सीधा आगे धकेलें।", "पैर वापस खींचकर स्टांस में रखें।", "पैर बदलें।"],
       T("8 each leg", "हर पैर 8"), MA_SAFE),
    sk("boxing", "drill", "box_shadow", "martialArts", "jab_cross", T("Shadow boxing round", "शैडो बॉक्सिंग राउंड"),
       T("Free-flowing punches and footwork for a full round.", "पूरे राउंड के लिए खुले पंच और फ़ुटवर्क।"),
       ["Start in your stance with hands up.", "Mix jabs, crosses, hooks and uppercuts.",
        "Move after every combination; never stand still.", "Breathe out with each punch."],
       ["हाथ ऊपर रखकर स्टांस में शुरू करें।", "जैब, क्रॉस, हुक और अपरकट मिलाएँ।", "हर संयोजन के बाद चलें; कभी स्थिर न रहें।", "हर पंच पर साँस छोड़ें।"],
       T("3 rounds of 2 minutes", "2 मिनट के 3 राउंड"), MA_SAFE),
    sk("self_defence", "stance", "sd_stance", "martialArts", "palm_strike", T("Safe stance (hands up, open)", "सुरक्षित मुद्रा (हाथ ऊपर, खुले)"),
       T("Calm, balanced and protected: the starting point for everything else.", "शांत, संतुलित और सुरक्षित: बाकी सब का शुरुआती बिंदु।"),
       ["Stand side-on, one foot forward, knees soft.", "Raise open hands in front of your chest, palms out.",
        "Keep your chin down and elbows in.", "Say 'Stop!' firmly as you take the stance."],
       ["तिरछे खड़े हों, एक पैर आगे, घुटने हल्के मुड़े।", "खुले हाथ छाती के सामने उठाएँ, हथेलियाँ बाहर।",
        "ठुड्डी नीचे और कोहनियाँ अंदर रखें।", "मुद्रा लेते समय दृढ़ता से 'रुको!' कहें।"],
       T("Practise 10 times", "10 बार अभ्यास"), MA_SAFE),
    sk("self_defence", "technique", "sd_palm", "martialArts", "palm_strike", T("Palm-heel strike", "हथेली की एड़ी से प्रहार"),
       T("A strong strike that's safer for your hand than a fist.", "मुट्ठी से ज़्यादा हाथ के लिए सुरक्षित, ताकतवर प्रहार।"),
       ["From the safe stance, step forward slightly.", "Push the heel of your palm forward, fingers back.",
        "Drive from the back foot and hip.", "Return to stance and move away."],
       ["सुरक्षित मुद्रा से थोड़ा आगे कदम रखें।", "हथेली की एड़ी आगे धकेलें, उँगलियाँ पीछे।", "पिछले पैर और कूल्हे से ज़ोर लगाएँ।", "मुद्रा में लौटें और दूर हटें।"],
       T("10 each side", "हर तरफ़ 10"), MA_SAFE),
    sk("self_defence", "technique", "sd_knee", "martialArts", "knee_strike", T("Close-range knee", "पास से घुटने का प्रहार"),
       T("For when someone is too close: create space, then leave.", "जब कोई बहुत पास हो: जगह बनाएँ, फिर निकल जाएँ।"),
       ["Bring your hands up in front.", "Drive the knee up and forward.", "Set the foot down behind you to step away.", "Alternate legs."],
       ["हाथ सामने ऊपर लाएँ।", "घुटना ऊपर और आगे लाएँ।", "दूर हटने के लिए पैर पीछे रखें।", "पैर बदलते रहें।"],
       T("10 each leg", "हर पैर 10"), MA_SAFE),
    sk("self_defence", "technique", "sd_elbow", "martialArts", "elbow_strike", T("Elbow strike at close range", "पास से कोहनी का प्रहार"),
       T("Your strongest close-range tool.", "पास की दूरी का आपका सबसे मज़बूत साधन।"),
       ["From the safe stance, raise the elbow to shoulder height.", "Turn the hips and swing the elbow across.",
        "Step back to create space.", "Repeat on the other side."],
       ["सुरक्षित मुद्रा से कोहनी कंधे तक उठाएँ।", "कूल्हे घुमाकर कोहनी आर-पार घुमाएँ।", "जगह बनाने के लिए पीछे हटें।", "दूसरी तरफ़ दोहराएँ।"],
       T("10 each side", "हर तरफ़ 10"), MA_SAFE),
    sk("self_defence", "technique", "sd_wrist_release", "martialArts", None, T("Wrist-grab release", "कलाई की पकड़ से छूटना"),
       T("Turn toward the gap between thumb and fingers, the weakest part of a grip.", "अंगूठे और उँगलियों के बीच की खाली जगह की ओर घुमाएँ, पकड़ का सबसे कमज़ोर हिस्सा।"),
       ["Notice where the thumb is on your wrist.", "Bend your elbow towards the person's thumb.",
        "Pull your arm out sharply through the gap.", "Step back and move away. Practise slowly with a trusted friend."],
       ["देखें कि आपकी कलाई पर अंगूठा कहाँ है।", "कोहनी को उस व्यक्ति के अंगूठे की ओर मोड़ें।",
        "खाली जगह से हाथ तेज़ी से बाहर खींचें।", "पीछे हटें और दूर जाएँ। किसी भरोसेमंद दोस्त के साथ धीरे अभ्यास करें।"],
       T("5 slow practices each side", "हर तरफ़ 5 धीमे अभ्यास"),
       T("Practise gently: the aim is to learn the angle, not to hurt anyone.", "हल्के अभ्यास करें: लक्ष्य कोण सीखना है, किसी को चोट पहुँचाना नहीं।")),
]

WORLD_PROGRAMS = [
    {"id": "muay_thai_basics", "category": "martialArts", "discipline": "muay_thai", "level": "beginner", "rounds": 2,
     "title": T("Muay Thai basics", "मुए थाई की शुरुआत"),
     "summary": T("Knees, elbows and push kicks with boxing footwork.", "बॉक्सिंग फ़ुटवर्क के साथ घुटने, कोहनी और पुश किक।"),
     "steps": [step("box_stance", 30, rest=10), step("mt_teep", 30, sides=True, rest=15), step("mt_knee", 30, rest=15),
               step("mt_elbow", 20, sides=True, rest=15), step("box_jab_cross", 30, rest=30)]},
    {"id": "self_defence_basics", "category": "martialArts", "discipline": "self_defence", "level": "beginner",
     "title": T("Self-defence basics", "आत्मरक्षा की बुनियाद"),
     "summary": T("Stance, voice and three simple strikes to create space.", "मुद्रा, आवाज़ और जगह बनाने के तीन सरल प्रहार।"),
     "steps": [step("sd_stance", 30, rest=10), step("sd_palm", 20, sides=True, rest=10),
               step("sd_knee", 20, sides=True, rest=10), step("sd_elbow", 20, sides=True, rest=10), step("sd_stance", 30, rest=0)]},
]

INDIAN = [
    # Kalaripayattu
    sk("kalaripayattu", "conditioning", "kalari_nerkal", "martialArts", "kalari_leg_swing", T("Straight leg kick (Nerkal)", "सीधी टांग किक (नेरकल)"),
       T("A classic kalari leg swing that builds flexibility and hip control.", "कलरी का पारंपरिक पैर उछाल जो लचीलापन और कूल्हों का नियंत्रण बढ़ाता है।"),
       ["Stand tall with arms extended in front at chest height.", "Swing one straight leg up towards your hands.",
        "Lower it with control and step forward.", "Alternate legs as you move across the floor."],
       ["हाथ छाती की ऊँचाई पर सामने फैलाकर सीधे खड़े हों।", "एक सीधी टांग हाथों की ओर ऊपर उछालें।",
        "नियंत्रण से नीचे लाएँ और आगे कदम रखें।", "फ़र्श पर आगे बढ़ते हुए पैर बदलते रहें।"],
       T("10 each leg", "हर पैर 10"), T("Warm up first and swing only as high as is comfortable.", "पहले वॉर्म-अप करें और उतना ही उछालें जितना आरामदायक हो।")),
    sk("kalaripayattu", "stance", "kalari_gaja", "martialArts", "kalari_elephant", T("Elephant stance (Gaja vadivu)", "गज वडिवु"),
       T("A deep, grounded stance; the arms move like an elephant's trunk.", "गहरी, स्थिर मुद्रा; हाथ हाथी की सूँड की तरह चलते हैं।"),
       ["Step into a deep forward stance.", "Lean the chest forward over the front knee.",
        "Join the hands low in front and sway them slowly.", "Hold, breathing through the nose; then switch sides."],
       ["गहरे आगे वाले स्टांस में आएँ।", "छाती को आगे वाले घुटने के ऊपर झुकाएँ।",
        "हाथ सामने नीचे जोड़ें और धीरे झुलाएँ।", "नाक से साँस लेते हुए रुकें; फिर तरफ़ बदलें।"],
       T("20–30 seconds each side", "हर तरफ़ 20–30 सेकंड"), MA_SAFE),
    sk("kalaripayattu", "stance", "kalari_simha", "martialArts", "kalari_lion", T("Lion stance (Simha vadivu)", "सिंह वडिवु"),
       T("Low and ready to spring, with clawed hands.", "नीचे और उछलने को तैयार, पंजे जैसे हाथ।"),
       ["Sink into a low stance with the back knee near the floor.", "Curl the fingers like claws near your face.",
        "Keep the back long and eyes forward.", "Hold, then switch sides."],
       ["पिछला घुटना ज़मीन के पास रखकर नीची मुद्रा में बैठें।", "उँगलियों को चेहरे के पास पंजों की तरह मोड़ें।",
        "पीठ लंबी और नज़र आगे रखें।", "रुकें, फिर तरफ़ बदलें।"],
       T("20 seconds each side", "हर तरफ़ 20 सेकंड"), MA_SAFE),
    sk("kalaripayattu", "stance", "kalari_ashwa", "martialArts", "kalari_horse", T("Horse stance (Ashwa vadivu)", "अश्व वडिवु"),
       T("A long, strong stance that builds the legs for kicks.", "लंबी, मज़बूत मुद्रा जो किक के लिए पैर बनाती है।"),
       ["Take a long stance, front knee bent, back leg long.", "Reach one arm forward and the other back.",
        "Keep the torso upright.", "Hold, then switch."],
       ["लंबा स्टांस लें, आगे का घुटना मुड़ा, पिछला पैर लंबा।", "एक हाथ आगे और दूसरा पीछे फैलाएँ।", "धड़ सीधा रखें।", "रुकें, फिर बदलें।"],
       T("20–30 seconds each side", "हर तरफ़ 20–30 सेकंड"), MA_SAFE),
    # Silambam
    sk("silambam", "drill", "silambam_kaaladi", "martialArts", "shuffle", T("Footwork (Kaaladi)", "कदम (कालडि)"),
       T("Silambam's foundation: light, rhythmic steps in patterns.", "सिलंबम की नींव: पैटर्न में हल्के, लयबद्ध कदम।"),
       ["Stand light on the balls of your feet.", "Step forward, back and to each side in a steady rhythm.",
        "Keep your knees soft and your head level.", "Add turns once the rhythm feels easy."],
       ["पंजों के आगे के हिस्से पर हल्के खड़े हों।", "स्थिर लय में आगे, पीछे और दोनों तरफ़ कदम रखें।",
        "घुटने हल्के मुड़े और सिर एक ऊँचाई पर रखें।", "लय आसान लगे तो घुमाव जोड़ें।"],
       T("1–2 minutes", "1–2 मिनट"), STICK_SAFE),
    sk("silambam", "technique", "silambam_figure8", "martialArts", "silambam_spin", T("Two-hand staff spin (figure-eight)", "दोनों हाथों से लाठी घुमाना (आठ का आकार)"),
       T("The signature silambam rotation, done slowly first.", "सिलंबम का खास घुमाव, पहले धीरे।"),
       ["Hold the staff in the middle with both hands, shoulder-width apart.", "Rotate it down on one side of the body and up on the other.",
        "Let the wrists turn smoothly.", "Change direction after 10 turns."],
       ["लाठी बीच से दोनों हाथों से कंधे जितनी दूरी पर पकड़ें।", "एक तरफ़ नीचे और दूसरी तरफ़ ऊपर घुमाएँ।",
        "कलाइयों को सहजता से घूमने दें।", "10 बार के बाद दिशा बदलें।"],
       T("3 sets of 10 turns", "10 घुमाव के 3 सेट"), STICK_SAFE),
    sk("silambam", "technique", "silambam_one_hand", "martialArts", "stick_twirl", T("One-hand twirl", "एक हाथ से घुमाना"),
       T("Wrist control with a short stick.", "छोटी छड़ी से कलाई का नियंत्रण।"),
       ["Hold a short stick near its middle in one hand.", "Turn it in circles in front of you using the wrist.",
        "Keep the elbow close to the body.", "Switch hands."],
       ["एक हाथ में छोटी छड़ी बीच के पास पकड़ें।", "कलाई से सामने गोल घुमाएँ।", "कोहनी शरीर के पास रखें।", "हाथ बदलें।"],
       T("30 seconds each hand", "हर हाथ 30 सेकंड"), STICK_SAFE),
    # Gatka
    sk("gatka", "drill", "gatka_pentra", "martialArts", "shuffle", T("Pentra (rhythmic footwork)", "पैंतरा (लयबद्ध कदम)"),
       T("Gatka's moving base: stepping in rhythm, always balanced.", "गतका का चलता आधार: लय में कदम, हमेशा संतुलित।"),
       ["Stand with feet shoulder-width apart, weight balanced.", "Step in a slow, steady rhythm: forward, back, side.",
        "Stay light and keep turning to face your direction.", "Speed up only when the rhythm is smooth."],
       ["पैर कंधे जितने खोलकर, वज़न बराबर रखकर खड़े हों।", "धीमी, स्थिर लय में कदम रखें: आगे, पीछे, बगल।",
        "हल्के रहें और अपनी दिशा की ओर मुड़ते रहें।", "लय सहज हो तभी गति बढ़ाएँ।"],
       T("1–2 minutes", "1–2 मिनट"), STICK_SAFE),
    sk("gatka", "technique", "gatka_overhead", "martialArts", "gatka_strike", T("Overhead stick strike", "ऊपर से छड़ी का वार"),
       T("Raise and strike down while stepping forward.", "आगे कदम रखते हुए उठाकर नीचे वार।"),
       ["Raise the stick over the shoulder.", "Step forward and bring it down in front of you.",
        "Stop the stick at chest height.", "Return to guard."],
       ["छड़ी कंधे के ऊपर उठाएँ।", "आगे कदम रखकर सामने नीचे लाएँ।", "छड़ी छाती की ऊँचाई पर रोकें।", "गार्ड में लौटें।"],
       T("10 each side", "हर तरफ़ 10"), STICK_SAFE),
    # Mardani Khel
    sk("mardani_khel", "technique", "mardani_twirl", "martialArts", "stick_twirl", T("Lathi twirl", "लाठी घुमाना"),
       T("Fast wrist rotations that Mardani Khel is famous for.", "तेज़ कलाई घुमाव जिनके लिए मर्दानी खेल प्रसिद्ध है।"),
       ["Hold a light stick in one hand.", "Rotate it in circles beside your body.",
        "Keep the elbow tucked and the wrist loose.", "Change sides and directions."],
       ["एक हाथ में हल्की छड़ी पकड़ें।", "शरीर के बगल में गोल घुमाएँ।", "कोहनी अंदर और कलाई ढीली रखें।", "तरफ़ और दिशा बदलें।"],
       T("30 seconds each side", "हर तरफ़ 30 सेकंड"), STICK_SAFE),
    sk("mardani_khel", "technique", "mardani_two_hand", "martialArts", "silambam_spin", T("Two-hand lathi rotation", "दोनों हाथों से लाठी घुमाना"),
       T("Builds shoulders and coordination.", "कंधे और तालमेल बनाता है।"),
       ["Hold the lathi with both hands.", "Rotate it in front of you, one end down then up.",
        "Move the feet with the rotation.", "Reverse direction."],
       ["लाठी दोनों हाथों से पकड़ें।", "सामने घुमाएँ, एक सिरा नीचे फिर ऊपर।", "घुमाव के साथ पैर चलाएँ।", "दिशा उलटें।"],
       T("3 sets of 30 seconds", "30 सेकंड के 3 सेट"), STICK_SAFE),
    # Thang-ta
    sk("thang_ta", "stance", "thangta_low", "martialArts", "thangta_stance", T("Low flowing stance", "नीची बहती मुद्रा"),
       T("Sarit-sarak style: sink low and flow from side to side.", "सरित-सरक शैली: नीचे बैठें और एक तरफ़ से दूसरी तरफ़ बहें।"),
       ["Sink into a long, low stance.", "Raise the front arm, the back arm guarding.",
        "Shift your weight smoothly to the other side.", "Keep the head level as you flow."],
       ["लंबी, नीची मुद्रा में बैठें।", "आगे वाला हाथ उठाएँ, पिछला बचाव में।", "वज़न सहजता से दूसरी तरफ़ ले जाएँ।", "बहते हुए सिर एक ऊँचाई पर रखें।"],
       T("1 minute", "1 मिनट"), MA_SAFE),
    sk("thang_ta", "technique", "thangta_palm", "martialArts", "palm_strike", T("Open-hand strike", "खुले हाथ का प्रहार"),
       T("A smooth unarmed strike from the low stance.", "नीची मुद्रा से सहज बिना हथियार का प्रहार।"),
       ["From the low stance, step through.", "Push the open palm forward.", "Return to guard.", "Switch sides."],
       ["नीची मुद्रा से आगे कदम रखें।", "खुली हथेली आगे धकेलें।", "गार्ड में लौटें।", "तरफ़ बदलें।"],
       T("10 each side", "हर तरफ़ 10"), MA_SAFE),
    # Kushti
    sk("kushti", "conditioning", "kushti_dand", "martialArts", "hindu_pushup", T("Dand (Hindu push-up)", "दंड"),
       T("The wrestler's push-up: a flowing swoop from hips-high to chest-up.", "पहलवान का पुश-अप: कूल्हे ऊपर से छाती ऊपर तक बहती गति।"),
       ["Start with hips high, hands and feet on the floor.", "Bend the elbows and swoop the chest forward close to the floor.",
        "Push up into an upward-facing arch.", "Push the hips back up to the start."],
       ["कूल्हे ऊपर, हाथ और पैर ज़मीन पर रखकर शुरू करें।", "कोहनियाँ मोड़कर छाती को ज़मीन के पास आगे लाएँ।",
        "ऊपर की ओर धकेलकर पीठ को धनुष जैसा मोड़ें।", "कूल्हे वापस ऊपर ले जाएँ।"],
       T("3 sets of 8–15", "8–15 के 3 सेट"), COND_SAFE),
    sk("kushti", "conditioning", "kushti_baithak", "martialArts", "hindu_squat", T("Baithak (Hindu squat)", "बैठक"),
       T("High-rep squats on the toes with an arm swing; legendary for leg stamina.", "पंजों पर बाँह झुलाते हुए ज़्यादा गिनती के स्क्वाट; पैरों की सहनशक्ति के लिए प्रसिद्ध।"),
       ["Stand with feet hip-width, arms back.", "Squat down, letting the heels lift, arms swinging forward.",
        "Rise up as the arms swing back.", "Keep a steady rhythm."],
       ["पैर कूल्हों जितने खोलकर, हाथ पीछे रखकर खड़े हों।", "एड़ियाँ उठने दें, हाथ आगे झुलाते हुए नीचे बैठें।",
        "हाथ पीछे झुलाते हुए उठें।", "स्थिर लय रखें।"],
       T("3 sets of 20–30", "20–30 के 3 सेट"), COND_SAFE),
    sk("kushti", "conditioning", "kushti_mugdar", "martialArts", "mugdar_swing", T("Mugdar swing (Indian club)", "मुग्दर घुमाना"),
       T("Swinging a club behind and around the shoulder for strong, mobile shoulders.", "कंधों को मज़बूत और गतिशील बनाने के लिए मुग्दर को पीछे और चारों ओर घुमाना।"),
       ["Start with a very light club or a filled water bottle.", "Let it drop behind the shoulder.",
        "Swing it out and up in front.", "Lower it with control; switch arms."],
       ["बहुत हल्के मुग्दर या भरी पानी की बोतल से शुरू करें।", "उसे कंधे के पीछे गिरने दें।",
        "बाहर और ऊपर सामने घुमाएँ।", "नियंत्रण से नीचे लाएँ; हाथ बदलें।"],
       T("2 sets of 10 each arm", "हर हाथ 10 के 2 सेट"),
       T("Learn the path with almost no weight. A heavy club can strain the shoulder or slip.", "लगभग बिना वज़न के रास्ता सीखें। भारी मुग्दर कंधे पर ज़ोर डाल सकता है या फिसल सकता है।")),
    sk("kushti", "stance", "kushti_stance", "martialArts", "wrestler_stance", T("Wrestling stance", "कुश्ती की मुद्रा"),
       T("Low, square and balanced, hands ready.", "नीची, सधी और संतुलित, हाथ तैयार।"),
       ["Feet wider than shoulders, one slightly forward.", "Bend the knees and hips; chest up.",
        "Hands in front, elbows in.", "Move in small steps without crossing the feet."],
       ["पैर कंधों से चौड़े, एक थोड़ा आगे।", "घुटने और कूल्हे मोड़ें; छाती ऊपर।", "हाथ सामने, कोहनियाँ अंदर।", "पैरों को क्रॉस किए बिना छोटे कदमों से चलें।"],
       T("3 × 30 seconds", "3 × 30 सेकंड"), MA_SAFE),
    sk("kushti", "drill", "kushti_sprawl", "martialArts", "sprawl", T("Sprawl", "स्प्रॉल"),
       T("Shoot the legs back to defend a takedown; great cardio.", "पटकनी से बचाव के लिए पैर पीछे फेंकें; बढ़िया कार्डियो।"),
       ["Start in wrestling stance.", "Drop the hands to the floor and shoot both legs back.",
        "Press the hips down.", "Snap back up into stance."],
       ["कुश्ती की मुद्रा में शुरू करें।", "हाथ ज़मीन पर रखकर दोनों पैर पीछे फेंकें।", "कूल्हे नीचे दबाएँ।", "तेज़ी से वापस मुद्रा में आएँ।"],
       T("3 sets of 8", "8 के 3 सेट"), COND_SAFE, "intermediate"),
    # Musti Yuddha
    sk("musti_yuddha", "stance", "musti_guard", "martialArts", "guard", T("Guard and footwork", "गार्ड और फ़ुटवर्क"),
       T("Fists up, chin down, light on the feet.", "मुट्ठियाँ ऊपर, ठुड्डी नीचे, पैरों पर हल्के।"),
       ["Stand side-on, fists by the cheeks.", "Move forward and back in small steps.",
        "Keep the elbows protecting the ribs.", "Stay relaxed."],
       ["तिरछे खड़े हों, मुट्ठियाँ गालों के पास।", "छोटे कदमों से आगे-पीछे चलें।", "कोहनियों से पसलियों की रक्षा करें।", "ढीले रहें।"],
       T("1 minute", "1 मिनट"), MA_SAFE),
    sk("musti_yuddha", "technique", "musti_straight", "martialArts", "jab_cross", T("Straight strikes", "सीधे प्रहार"),
       T("Fast, straight fist strikes from the guard.", "गार्ड से तेज़, सीधे मुट्ठी प्रहार।"),
       ["From guard, strike straight with the lead fist.", "Bring it back as the rear fist strikes.",
        "Turn the back foot with the rear strike.", "Return to guard."],
       ["गार्ड से आगे वाली मुट्ठी से सीधा प्रहार करें।", "उसे वापस लाते हुए पिछली मुट्ठी से प्रहार करें।",
        "पिछले प्रहार के साथ पिछला पैर घुमाएँ।", "गार्ड में लौटें।"],
       T("3 rounds of 30 seconds", "30 सेकंड के 3 राउंड"), MA_SAFE),
    # Lathi Khela
    sk("lathi_khela", "technique", "lathi_block_high", "martialArts", "lathi_block", T("High block with the lathi", "लाठी से ऊपरी बचाव"),
       T("Raise the staff to protect the head.", "सिर बचाने के लिए लाठी उठाएँ।"),
       ["Hold the lathi with both hands, shoulder-width apart.", "Raise it above your head, held across.",
        "Step slightly forward as you block.", "Lower to guard."],
       ["लाठी को दोनों हाथों से कंधे जितनी दूरी पर पकड़ें।", "उसे सिर के ऊपर आड़ा उठाएँ।", "बचाव करते समय थोड़ा आगे कदम रखें।", "गार्ड में नीचे लाएँ।"],
       T("10 repetitions", "10 बार"), STICK_SAFE),
    sk("lathi_khela", "technique", "lathi_overhead", "martialArts", "lathi_strike", T("Overhead two-hand strike", "ऊपर से दोनों हाथों का वार"),
       T("A downward strike with a forward step.", "आगे कदम के साथ नीचे की ओर वार।"),
       ["Raise the lathi overhead with both hands.", "Step forward and bring it down in front.",
        "Stop it at chest height.", "Return to guard."],
       ["दोनों हाथों से लाठी सिर के ऊपर उठाएँ।", "आगे कदम रखकर सामने नीचे लाएँ।", "छाती की ऊँचाई पर रोकें।", "गार्ड में लौटें।"],
       T("10 repetitions", "10 बार"), STICK_SAFE),
]

INDIAN_PROGRAMS = [
    {"id": "kalari_basics", "category": "martialArts", "discipline": "kalaripayattu", "level": "beginner",
     "title": T("Kalari basics (Meippayattu)", "कलरी की शुरुआत (मेइप्पयट्टु)"),
     "summary": T("Leg swings and animal stances to build flexibility and control.", "लचीलेपन और नियंत्रण के लिए पैर उछाल और पशु मुद्राएँ।"),
     "steps": [step("kalari_nerkal", 40, rest=15), step("kalari_gaja", 25, sides=True, rest=10),
               step("kalari_ashwa", 25, sides=True, rest=10), step("kalari_simha", 20, sides=True, rest=10),
               step("kalari_nerkal", 40, rest=0)]},
    {"id": "akhara_conditioning", "category": "martialArts", "discipline": "kushti", "level": "intermediate", "rounds": 3,
     "title": T("Akhara conditioning (Dand-Baithak)", "अखाड़ा कसरत (दंड-बैठक)"),
     "summary": T("The wrestler's classic: dand, baithak and sprawls.", "पहलवान की पारंपरिक कसरत: दंड, बैठक और स्प्रॉल।"),
     "steps": [step("kushti_dand", reps=10, rest=20), step("kushti_baithak", reps=25, rest=20),
               step("kushti_sprawl", reps=6, rest=20), step("kushti_stance", 30, rest=45)]},
    {"id": "stick_drills", "category": "martialArts", "discipline": "silambam", "level": "beginner",
     "title": T("Stick drills (Silambam & Lathi)", "छड़ी अभ्यास (सिलंबम और लाठी)"),
     "summary": T("Footwork, spins, blocks and strikes with a light stick.", "हल्की छड़ी से फ़ुटवर्क, घुमाव, बचाव और वार।"),
     "steps": [step("silambam_kaaladi", 45, rest=10), step("silambam_figure8", 40, rest=15), step("silambam_one_hand", 30, sides=True, rest=10),
               step("lathi_block_high", 30, rest=10), step("lathi_overhead", 30, rest=0)]},
    {"id": "gatka_mardani", "category": "martialArts", "discipline": "gatka", "level": "beginner",
     "title": T("Gatka & Mardani Khel drills", "गतका और मर्दानी खेल अभ्यास"),
     "summary": T("Pentra footwork, overhead strikes and lathi rotations.", "पैंतरा फ़ुटवर्क, ऊपर से वार और लाठी घुमाव।"),
     "steps": [step("gatka_pentra", 45, rest=10), step("gatka_overhead", 30, sides=True, rest=15),
               step("mardani_twirl", 30, sides=True, rest=10), step("mardani_two_hand", 30, rest=0)]},
]


def apply(packs):
    m = packs["martial-arts"]
    for e in m["exercises"]:
        if e["id"] in TAGS:
            e["discipline"], e["kind"] = TAGS[e["id"]]
    for p in m["programs"]:
        if p["id"] in PROGRAM_TAGS:
            p["discipline"] = PROGRAM_TAGS[p["id"]]
    m["exercises"] = m["exercises"] + WORLD_EXTRA
    m["programs"] = m["programs"] + WORLD_PROGRAMS
    m["version"] = 2
    m["summary"] = T("Boxing, Muay Thai, karate, kung fu and self-defence: solo techniques and drills, no sparring.",
                     "बॉक्सिंग, मुए थाई, कराटे, कुंग फ़ू और आत्मरक्षा: अकेले की तकनीक और अभ्यास, कोई स्पारिंग नहीं।")
    for e in m["exercises"]:
        if e.get("motion") is None:
            e.pop("motion", None)
    packs["indian-martial-arts"] = {
        "version": 1,
        "title": T("Indian martial arts", "भारतीय युद्ध-कलाएँ"),
        "summary": T("Kalaripayattu, Silambam, Gatka, Mardani Khel, Thang-ta, Kushti, Musti Yuddha and Lathi Khela: stances, footwork, stick drills and akhara conditioning.",
                     "कलरीपयट्टु, सिलंबम, गतका, मर्दानी खेल, थांग-ता, कुश्ती, मुष्टि युद्ध और लाठी खेला: मुद्राएँ, फ़ुटवर्क, छड़ी अभ्यास और अखाड़ा कसरत।"),
        "exercises": INDIAN, "programs": INDIAN_PROGRAMS}
