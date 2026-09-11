"""
Expand Phase 5 slider to include IMG_0786, IMG_0841, and IMG_0851, bringing total to 7 curated photos:
Slide 1: Date Night in London (Lost Oasis • 2025)
Slide 2: An Epic Proposal (London City Nights • 2025)
Slide 3: London Nights (Counting Down to Forever • 2025/2026)
Slide 4: City Nights & Embrace (IMG_0786 - London • 2026)
Slide 5: Pure Joy & Laughter (IMG_0841 - Playful Hearts • 2026)
Slide 6: Devotion & Grace (IMG_0851 - Black Tie Editorial • 2026)
Slide 7: The Next Chapter (IMG_0855 - London to Accra • 09.01.2027)
"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

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
                <!-- Slide 4: Engagement Shoot Signature -->
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
              <div class="story-slider-counter">1 / 4</div>
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
            </div>
          </div>"""

new_phase5_media = """                    <div class="story-frame story-slider-frame" data-slider-id="phase-5">
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

assert old_phase5_media in content, "old_phase5_media not found in index.html"
content = content.replace(old_phase5_media, new_phase5_media, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("wedding-index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully updated Phase 5 with 7 photos and 100% parity across index.html and wedding-index.html!")
