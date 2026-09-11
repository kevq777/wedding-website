"""
Reorganize Story Timeline:
1. Phase 4: Move London Nights (mirror selfie 2025) and Date Night in London (Lost Oasis 2025) into Phase 4, expanding it from 4 to 6 slides.
   Update Phase 4 counter to 1 / 6, add dots 5 & 6, and update captions.
   Update milestone badge to 2020 – 2025 • Together in the UK.
2. Phase 5: Update 'An Epic Proposal' subtitle to 2026.
   Add Shannel showing the ring (story-phase5-ring-hand.webp) and IMG_0916 rooftop skyline (story-phase5-rooftop-ring.webp).
   Phase 5 now has 7 purely 2026 engagement editorial photos.
   Update milestone badge to 2026 – 2027 • The Covenant.
3. Synchronize 100% byte-for-byte between index.html and wedding-index.html.
"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# --- 1. PHASE 4 REPLACEMENT ---
old_phase4_media = """                    <div class="story-frame story-slider-frame" data-slider-id="phase-4">
            <div class="story-frame-inner">
              <div class="story-slider-track">
                <!-- Slide 1: Reunited in UK Courtyard -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase4-01-reunited-uk.webp" 
                    alt="Kevin and Shannel reunited together in the UK" 
                    loading="lazy"
                    width="549"
                    height="800"
                    style="object-position: center 12%;"
                  />
                </div>
                <!-- Slide 2: Gym in UK 2020 -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase4-02-gym.webp" 
                    alt="Gym training together in the UK in 2020" 
                    loading="lazy"
                    width="428"
                    height="800"
                    style="object-position: center 48%;"
                  />
                </div>
                <!-- Slide 3: Workout progression -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase4-03-workout.webp" 
                    alt="Workout progression and mutual goals" 
                    loading="lazy"
                    width="428"
                    height="800"
                    style="object-position: center 25%;"
                  />
                </div>
                <!-- Slide 4: 2024 UK life -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase4-04-uk2024.webp" 
                    alt="Building our life in the UK together" 
                    loading="lazy"
                    width="600"
                    height="800"
                    style="object-position: center 15%;"
                  />
                </div>
              </div>

              <!-- Slider Navigation Controls -->
              <button class="story-slider-btn prev" aria-label="Previous photo">&#8249;</button>
              <button class="story-slider-btn next" aria-label="Next photo">&#8250;</button>
              <div class="story-slider-counter">1 / 4</div>
            </div>

            <!-- Synchronized Captions Track -->
            <div class="story-frame-captions">
              <div class="story-frame-caption active">
                Reunited in the UK
                <span>Doctor &amp; Engineer &bull; Finally Together</span>
              </div>
              <div class="story-frame-caption">
                Gym &amp; Growth Together
                <span>Supporting Each Other's Goals &bull; 2020</span>
              </div>
              <div class="story-frame-caption">
                Dedication &amp; Progress
                <span>Health &amp; Life in the UK</span>
              </div>
              <div class="story-frame-caption">
                A Life Built Together
                <span>United in the UK</span>
              </div>
            </div>

            <!-- Slider Pagination Dots -->
            <div class="story-slider-nav" aria-label="Phase 4 photo navigation">
              <button class="story-slider-dot active" aria-label="Photo 1"></button>
              <button class="story-slider-dot" aria-label="Photo 2"></button>
              <button class="story-slider-dot" aria-label="Photo 3"></button>
              <button class="story-slider-dot" aria-label="Photo 4"></button>
            </div>
          </div>"""

new_phase4_media = """                    <div class="story-frame story-slider-frame" data-slider-id="phase-4">
            <div class="story-frame-inner">
              <div class="story-slider-track">
                <!-- Slide 1: Reunited in UK Courtyard -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase4-01-reunited-uk.webp" 
                    alt="Kevin and Shannel reunited together in the UK" 
                    loading="lazy"
                    width="549"
                    height="800"
                    style="object-position: center 12%;"
                  />
                </div>
                <!-- Slide 2: Gym in UK 2020 -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase4-02-gym.webp" 
                    alt="Gym training together in the UK in 2020" 
                    loading="lazy"
                    width="428"
                    height="800"
                    style="object-position: center 48%;"
                  />
                </div>
                <!-- Slide 3: Workout progression -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase4-03-workout.webp" 
                    alt="Workout progression and mutual goals" 
                    loading="lazy"
                    width="428"
                    height="800"
                    style="object-position: center 25%;"
                  />
                </div>
                <!-- Slide 4: 2024 UK life -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase4-04-uk2024.webp" 
                    alt="Building our life in the UK together" 
                    loading="lazy"
                    width="600"
                    height="800"
                    style="object-position: center 15%;"
                  />
                </div>
                <!-- Slide 5: Date Night in London (2025) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-01-shannel29.webp" 
                    alt="Date night celebrating in London" 
                    loading="lazy"
                    width="600"
                    height="800"
                    style="object-position: center 5%;"
                  />
                </div>
                <!-- Slide 6: London Nights (2025) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-03-date2025.webp" 
                    alt="Kevin and Shannel celebrating in London" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>
              </div>

              <!-- Slider Navigation Controls -->
              <button class="story-slider-btn prev" aria-label="Previous photo">&#8249;</button>
              <button class="story-slider-btn next" aria-label="Next photo">&#8250;</button>
              <div class="story-slider-counter">1 / 6</div>
            </div>

            <!-- Synchronized Captions Track -->
            <div class="story-frame-captions">
              <div class="story-frame-caption active">
                Reunited in the UK
                <span>Doctor &amp; Engineer &bull; Finally Together</span>
              </div>
              <div class="story-frame-caption">
                Gym &amp; Growth Together
                <span>Supporting Each Other's Goals &bull; 2020</span>
              </div>
              <div class="story-frame-caption">
                Dedication &amp; Progress
                <span>Health &amp; Life in the UK</span>
              </div>
              <div class="story-frame-caption">
                A Life Built Together
                <span>United in the UK &bull; 2024</span>
              </div>
              <div class="story-frame-caption">
                Date Night in London
                <span>Lost Oasis &bull; 2025</span>
              </div>
              <div class="story-frame-caption">
                London Nights
                <span>Counting Down to Forever &bull; 2025</span>
              </div>
            </div>

            <!-- Slider Pagination Dots -->
            <div class="story-slider-nav" aria-label="Phase 4 photo navigation">
              <button class="story-slider-dot active" aria-label="Photo 1"></button>
              <button class="story-slider-dot" aria-label="Photo 2"></button>
              <button class="story-slider-dot" aria-label="Photo 3"></button>
              <button class="story-slider-dot" aria-label="Photo 4"></button>
              <button class="story-slider-dot" aria-label="Photo 5"></button>
              <button class="story-slider-dot" aria-label="Photo 6"></button>
            </div>
          </div>"""

assert old_phase4_media in content, "old_phase4_media not found"
content = content.replace(old_phase4_media, new_phase4_media, 1)

# Phase 4 badge update
content = content.replace(
    '<span class="story-milestone-badge">2020 – 2023 &bull; Perseverance</span>',
    '<span class="story-milestone-badge">2020 – 2025 &bull; Together in the UK</span>',
    1
)

# --- 2. PHASE 5 REPLACEMENT ---
old_phase5_media = """                    <div class="story-frame story-slider-frame" data-slider-id="phase-5">
            <div class="story-frame-inner">
              <div class="story-slider-track">
                <!-- Slide 1: Date Night in London -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-01-shannel29.webp" 
                    alt="Date night celebrating in London" 
                    loading="lazy"
                    width="600"
                    height="800"
                    style="object-position: center 5%;"
                  />
                </div>
                <!-- Slide 2: An Epic Proposal 2025 -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-02-epicshot.webp" 
                    alt="Kevin and Shannel embracing on their engagement proposal night in London" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>
                <!-- Slide 3: 2025 London Date -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-03-date2025.webp" 
                    alt="Kevin and Shannel celebrating in London" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>
                <!-- Slide 4: City Nights & Embrace (IMG_0786) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-04-streetembrace.webp" 
                    alt="Kevin embracing Shannel in elegant black attire under London streetlights" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>
                <!-- Slide 5: Pure Joy & Laughter (IMG_0841) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-05-playfuljoy.webp" 
                    alt="Shannel playfully posing and dancing while Kevin smiles up from the armchair" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>
                <!-- Slide 6: Devotion & Grace (IMG_0851) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-06-formaldignity.webp" 
                    alt="Formal portrait with Kevin seated and Shannel standing with hands on his shoulders" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>
                <!-- Slide 7: The Next Chapter -->
                <div class="story-slide">
                  <img 
                    src="assets/images/IMG_0855.webp" 
                    alt="Kevin and Shannel smiling together celebrating their upcoming wedding" 
                    loading="lazy"
                    width="900"
                    height="1100"
                    style="object-position: center 15%;"
                  />
                </div>
              </div>

              <!-- Slider Navigation Controls -->
              <button class="story-slider-btn prev" aria-label="Previous photo">&#8249;</button>
              <button class="story-slider-btn next" aria-label="Next photo">&#8250;</button>
              <div class="story-slider-counter">1 / 7</div>
            </div>

            <!-- Synchronized Captions Track -->
            <div class="story-frame-captions">
              <div class="story-frame-caption active">
                Date Night in London
                <span>Lost Oasis &bull; 2025</span>
              </div>
              <div class="story-frame-caption">
                An Epic Proposal
                <span>London City Nights &bull; 2025</span>
              </div>
              <div class="story-frame-caption">
                London Nights
                <span>Counting Down to Forever &bull; 2025/2026</span>
              </div>
              <div class="story-frame-caption">
                City Nights &amp; Embrace
                <span>London &bull; 2026</span>
              </div>
              <div class="story-frame-caption">
                Pure Joy &amp; Laughter
                <span>Playful Hearts &bull; 2026</span>
              </div>
              <div class="story-frame-caption">
                Devotion &amp; Grace
                <span>Black Tie Editorial &bull; 2026</span>
              </div>
              <div class="story-frame-caption">
                The Next Chapter
                <span>London to Accra &bull; 09.01.2027</span>
              </div>
            </div>

            <!-- Slider Pagination Dots -->
            <div class="story-slider-nav" aria-label="Phase 5 photo navigation">
              <button class="story-slider-dot active" aria-label="Photo 1"></button>
              <button class="story-slider-dot" aria-label="Photo 2"></button>
              <button class="story-slider-dot" aria-label="Photo 3"></button>
              <button class="story-slider-dot" aria-label="Photo 4"></button>
              <button class="story-slider-dot" aria-label="Photo 5"></button>
              <button class="story-slider-dot" aria-label="Photo 6"></button>
              <button class="story-slider-dot" aria-label="Photo 7"></button>
            </div>
          </div>"""

new_phase5_media = """                    <div class="story-frame story-slider-frame" data-slider-id="phase-5">
            <div class="story-frame-inner">
              <div class="story-slider-track">
                <!-- Slide 1: An Epic Proposal (2026) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-02-epicshot.webp" 
                    alt="Kevin and Shannel embracing on their engagement proposal night in London" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>
                <!-- Slide 2: The Ring & The Smile (IMG_0809) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-ring-hand.webp" 
                    alt="Shannel holding out her hand showing engagement ring with a radiant smile" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>
                <!-- Slide 3: Twilight Skyline (IMG_0916) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-rooftop-ring.webp" 
                    alt="Kevin and Shannel holding hands on the rooftop terrace showing the engagement ring" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>
                <!-- Slide 4: City Nights & Embrace (IMG_0786) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-04-streetembrace.webp" 
                    alt="Kevin embracing Shannel in elegant black attire under London streetlights" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>
                <!-- Slide 5: Pure Joy & Laughter (IMG_0841) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-05-playfuljoy.webp" 
                    alt="Shannel playfully posing and dancing while Kevin smiles up from the armchair" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>
                <!-- Slide 6: Devotion & Grace (IMG_0851) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-06-formaldignity.webp" 
                    alt="Formal portrait with Kevin seated and Shannel standing with hands on his shoulders" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>
                <!-- Slide 7: The Next Chapter (IMG_0855) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/IMG_0855.webp" 
                    alt="Kevin and Shannel smiling together celebrating their upcoming wedding" 
                    loading="lazy"
                    width="900"
                    height="1100"
                    style="object-position: center 15%;"
                  />
                </div>
              </div>

              <!-- Slider Navigation Controls -->
              <button class="story-slider-btn prev" aria-label="Previous photo">&#8249;</button>
              <button class="story-slider-btn next" aria-label="Next photo">&#8250;</button>
              <div class="story-slider-counter">1 / 7</div>
            </div>

            <!-- Synchronized Captions Track -->
            <div class="story-frame-captions">
              <div class="story-frame-caption active">
                An Epic Proposal
                <span>London City Nights &bull; 2026</span>
              </div>
              <div class="story-frame-caption">
                The Ring &amp; The Smile
                <span>She Said Yes &bull; London 2026</span>
              </div>
              <div class="story-frame-caption">
                Twilight Skyline
                <span>Holding Hands Under London Skies &bull; 2026</span>
              </div>
              <div class="story-frame-caption">
                City Nights &amp; Embrace
                <span>London &bull; 2026</span>
              </div>
              <div class="story-frame-caption">
                Pure Joy &amp; Laughter
                <span>Playful Hearts &bull; 2026</span>
              </div>
              <div class="story-frame-caption">
                Devotion &amp; Grace
                <span>Black Tie Editorial &bull; 2026</span>
              </div>
              <div class="story-frame-caption">
                The Next Chapter
                <span>London to Accra &bull; 09.01.2027</span>
              </div>
            </div>

            <!-- Slider Pagination Dots -->
            <div class="story-slider-nav" aria-label="Phase 5 photo navigation">
              <button class="story-slider-dot active" aria-label="Photo 1"></button>
              <button class="story-slider-dot" aria-label="Photo 2"></button>
              <button class="story-slider-dot" aria-label="Photo 3"></button>
              <button class="story-slider-dot" aria-label="Photo 4"></button>
              <button class="story-slider-dot" aria-label="Photo 5"></button>
              <button class="story-slider-dot" aria-label="Photo 6"></button>
              <button class="story-slider-dot" aria-label="Photo 7"></button>
            </div>
          </div>"""

assert old_phase5_media in content, "old_phase5_media not found"
content = content.replace(old_phase5_media, new_phase5_media, 1)

# Phase 5 badge update
content = content.replace(
    '<span class="story-milestone-badge">2024 – 2027 &bull; The Covenant</span>',
    '<span class="story-milestone-badge">2026 – 2027 &bull; The Covenant</span>',
    1
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("wedding-index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully reorganized story timeline with 100% parity across index.html and wedding-index.html!")
