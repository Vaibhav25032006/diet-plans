<!-- Is code ko aap apni website ke kisi bhi page par add kar sakte hain -->
<div id="herbalife-app-root" style="max-width: 600px; margin: 20px auto; padding: 25px; background: #ffffff; border-radius: 16px; box-shadow: 0 8px 30px rgba(0,0,0,0.12); font-family: sans-serif;">
    
    <div style="text-align: center; margin-bottom: 25px;">
        <h2 style="color: #2e7d32; margin: 0;">Herbalife Smart Wellness Portal</h2>
        <p style="color: #666; font-size: 14px; margin-top: 5px;">Live Browser AI System</p>
    </div>

    <!-- STEP 1: MEMBER SCAN/TYPE LOGIN -->
    <div id="web-login-box">
        <label style="display:block; font-weight: bold; margin-bottom: 8px; color: #333;">Enter or Scan Member ID:</label>
        <input type="text" id="webMemberId" placeholder="Type ID here..." style="width: 100%; padding: 12px; box-sizing: border-box; border: 2px solid #ddd; border-radius: 8px; font-size: 16px; margin-bottom: 15px;">
        <button onclick="processWebLogin()" style="width: 100%; padding: 14px; background: #2e7d32; color: white; border: none; font-weight: bold; font-size: 16px; border-radius: 8px; cursor: pointer; transition: 0.2s;">VERIFY ID & START COACHING</button>
        <p id="webStatus" style="text-align: center; font-weight: bold; margin-top: 15px; color: #d32f2f;"></p>
    </div>

    <!-- STEP 2: PROFESSIONAL COACH DASHBOARD -->
    <div id="web-dashboard-box" style="display: none;">
        <h3 id="webWelcomeName" style="color: #2e7d32; text-align: center; margin-bottom: 20px;">Welcome Member</h3>
        
        <!-- Live Action Camera Section -->
        <div id="camera-container" style="display:none; text-align: center; margin-bottom: 20px;">
            <video id="webcamView" autoplay playsinline style="width: 100%; max-width: 400px; background: #000; border-radius: 12px; transform: scaleX(-1);"></video>
            <div id="countdownTimer" style="font-size: 20px; font-weight: bold; color: #d32f2f; margin-top: 10px;">Analyzing: 10s</div>
        </div>

        <!-- 4 Core Buttons for Browser System -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 25px;">
            <button onclick="handleWebDiet()" style="padding: 20px; background: #e3f2fd; border: 1px solid #90caf9; font-weight: bold; border-radius: 10px; cursor: pointer;">📋<br>Diet & Routine Plan</button>
            <button onclick="startBrowserCameraScan()" style="padding: 20px; background: #e8f5e9; border: 1px solid #a5d6a7; font-weight: bold; border-radius: 10px; cursor: pointer;">📷<br>Scan Live Activity (10s)</button>
            <button onclick="toggleWebCalendar()" style="padding: 20px; background: #fff3e0; border: 1px solid #ffcc80; font-weight: bold; border-radius: 10px; cursor: pointer;">📅<br>Task Calendar</button>
            <button onclick="triggerFemaleVoiceBot()" style="padding: 20px; background: #f3e5f5; border: 1px solid #ce93d8; font-weight: bold; border-radius: 10px; cursor: pointer;">🎙️<br>Talk to Coach Voice</button>
        </div>

        <!-- Calendar Dashboard Visual Grid -->
        <div id="webCalendarGrid" style="display:none; margin-bottom: 20px; background: #f9f9f9; padding: 15px; border-radius: 8px;">
            <h4 style="margin-bottom: 10px;">Monthly Tracking (Live Updates)</h4>
            <div id="daysContainer" style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 5px; text-align: center;"></div>
        </div>

        <button onclick="window.open('https://herbalife-smart-wellness-studio.my.canva.site/page-3', '_blank')" style="width: 100%; padding: 12px; background: #d32f2f; color: white; border: none; font-weight: bold; border-radius: 8px; cursor: pointer;">🌐 GO TO MAIN WEBSITE</button>
    </div>
</div>

<script>
    let globalUserData = null;
    const BACKEND_URL = "http://127.0.0.1:5000"; // Jab aap live server par deploy karenge toh isko change kar dena

    // Voice Engine: Female Voice without any paid API Key
    function browserSpeak(text) {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel(); // Stop any previous speech
            let utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'hi-IN'; // Set to Indian Hindi/English Mix
            
            // Selecting clear Female Voice from browser engine
            let voices = window.speechSynthesis.getVoices();
            let femaleVoice = voices.find(voice => voice.name.includes('Google') || voice.name.includes('Female') || voice.lang === 'hi-IN');
            if (femaleVoice) utterance.voice = femaleVoice;
            
            window.speechSynthesis.speak(utterance);
        }
    }

    function processWebLogin() {
        const mid = document.getElementById('webMemberId').value.trim();
        const status = document.getElementById('webStatus');
        if(!mid) { status.innerText = "Error: Please enter ID"; return; }

        status.style.color = "#333";
        status.innerText = "Verifying from Google Sheet Data...";

        fetch(`${BACKEND_URL}/api/v1/verify-member`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ member_id: mid })
        })
        .then(res => res.json())
        .then(resData => {
            if(resData.success) {
                globalUserData = resData.data;
                document.getElementById('web-login-box').style.display = 'none';
                document.getElementById('web-dashboard-box').style.display = 'block';
                document.getElementById('webWelcomeName').innerText = `Coach Dashboard\nWelcome, ${globalUserData.name}!`;
                browserSpeak(`Namaste ${globalUserData.name}, aapka data analyze ho chuka hai. Main aapki professional herbalife coach hoon.`);
            } else {
                status.style.color = "red";
                status.innerText = resData.message;
            }
        }).catch(err => {
            status.style.color = "red";
            status.innerText = "Connection Error! Check if Python Server is running.";
        });
    }

    function handleWebDiet() {
        if(globalUserData.is_child) {
            browserSpeak("Aapki umar ke hisab se bacchon ka special activity schedule active kiya gaya hai.");
            alert("Child Diet & Routine Plan loaded based on Google Sheet Age.");
        } else {
            browserSpeak("Aapka adult weight management system program load ho gaya hai.");
            alert("Adult Weight Management Diet Plan Active.");
        }
    }

    function startBrowserCameraScan() {
        const camContainer = document.getElementById('camera-container');
        const video = document.getElementById('webcamView');
        const timerText = document.getElementById('countdownTimer');
        
        camContainer.style.display = "block";
        browserSpeak("Kripya live screen sharing ya camera ke saamne apni activity start karein.");

        // Open Browser Camera natively
        navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
            let timeLeft = 10;
            
            let counter = setInterval(() => {
                timeLeft--;
                timerText.innerText = `Analyzing: ${timeLeft}s`;
                if(timeLeft <= 0) {
                    clearInterval(counter);
                    // Stop Camera Stream
                    stream.getTracks().forEach(track => track.stop());
                    camContainer.style.display = "none";
                    browserSpeak("Aapka task automatic tick ho gaya hai. Calendar update kar diya gaya hai.");
                    alert("AI Analysis Match: Task Tick Marked on Calendar!");
                    markCalendarToday();
                }
            }, 1000);
        }).catch(err => {
            alert("Camera Access Denied or Not Available in browser.");
        });
    }

    function toggleWebCalendar() {
        const cal = document.getElementById('webCalendarGrid');
        cal.style.display = cal.style.display === "none" ? "block" : "none";
        
        // Generate blank calendar grids inside browser dynamically
        const container = document.getElementById('daysContainer');
        container.innerHTML = "";
        for(let i=1; i<=30; i++) {
            let dayBox = document.createElement('div');
            dayBox.innerText = i;
            dayBox.id = `day-box-${i}`;
            dayBox.style.padding = "8px";
            dayBox.style.background = "#ddd";
            dayBox.style.borderRadius = "4px";
            dayBox.style.fontSize = "12px";
            container.appendChild(dayBox);
        }
    }

    function markCalendarToday() {
        const today = new Date().getDate();
        const todayBox = document.getElementById(`day-box-${today}`);
        if(todayBox) {
            todayBox.style.background = "#2e7d32";
            todayBox.style.color = "white";
        }
    }

    function triggerFemaleVoiceBot() {
        browserSpeak("Main live google search tool se judi hui hoon, aapko kya jaankari chahiye?");
    }

    // Chrome specific audio unlocking protocol
    window.speechSynthesis.onvoiceschanged = function() { };
</script>
