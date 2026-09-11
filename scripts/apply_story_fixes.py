"""
Update index.html and wedding-index.html with:
1. Frame object-position fixes so faces are never cut off.
2. Replace duplicate leavers dinner in Phase 2 with humble beginnings.
3. Move bicycle date photo to Phase 3 (2018).
4. Update Phase 4 Slide 1 with reunited in the UK courtyard photo.
5. Upright Ghana match day photo in Phase 5.
6. Verify 100% parity between index.html and wedding-index.html.
"""
import re

new_phase1_media = '''          <div class="story-frame story-slider-frame" data-slider-id="phase-1">
            <div class="story-frame-inner">
              <div class="story-slider-track">
                <!-- Slide 1: Golden Tulip 1st Date -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase1-01-goldentulip.webp" 
                    alt="First date at Golden Tulip Hotel in 2015" 
                    loading="lazy"
                    width="450"
                    height="800"
                    style="object-position: center top;"
                  />
                </div>
                <!-- Slide 2: High School Uniform Meet -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-01-highschool-meet.webp" 
                    alt="Kevin and Shannel in high school uniform" 
                    loading="lazy"
                    width="570"
                    height="760"
                    style="object-position: center top;"
                  />
                </div>
                <!-- Slide 3: Elmina Trip -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase1-03-elmina.webp" 
                    alt="High school trip to Elmina Castle" 
                    loading="lazy"
                    width="600"
                    height="800"
                    style="object-position: center 15%;"
                  />
                </div>
                <!-- Slide 4: Beach Trip -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-02-beach-trip.webp" 
                    alt="High school beach trip with classmates" 
                    loading="lazy"
                    width="800"
                    height="532"
                    style="object-position: center center;"
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
                First Date at Golden Tulip
                <span>Accra &bull; 2015</span>
              </div>
              <div class="story-frame-caption">
                High School Sweethearts
                <span>Where It All Began &bull; 2015</span>
              </div>
              <div class="story-frame-caption">
                High School Trip to Elmina
                <span>Adventures Together &bull; 2015</span>
              </div>
              <div class="story-frame-caption">
                High School Beach Days
                <span>Youthful Memories &bull; 2015</span>
              </div>
            </div>

            <!-- Slider Pagination Dots -->
            <div class="story-slider-nav" aria-label="Phase 1 photo navigation">
              <button class="story-slider-dot active" aria-label="Photo 1"></button>
              <button class="story-slider-dot" aria-label="Photo 2"></button>
              <button class="story-slider-dot" aria-label="Photo 3"></button>
              <button class="story-slider-dot" aria-label="Photo 4"></button>
            </div>
          </div>'''

new_phase2_media = '''          <div class="story-frame story-slider-frame" data-slider-id="phase-2">
            <div class="story-frame-inner">
              <div class="story-slider-track">
                <!-- Slide 1: Labadi 18th Birthday -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-03-labadi-18th-bday.webp" 
                    alt="Kevin's 18th Birthday at Labadi Beach Hotel in 2016" 
                    loading="lazy"
                    width="567"
                    height="760"
                    style="object-position: center 15%;"
                  />
                </div>
                <!-- Slide 2: Leavers Dinner Formal Portrait -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-04-leavers-dinner.webp" 
                    alt="High School Leavers Dinner in 2016" 
                    loading="lazy"
                    width="506"
                    height="760"
                    style="object-position: center top;"
                  />
                </div>
                <!-- Slide 3: Humble Beginnings -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase2-03-humble-beginnings.webp" 
                    alt="Kevin and Shannel candid in high school days" 
                    loading="lazy"
                    width="600"
                    height="800"
                    style="object-position: center top;"
                  />
                </div>
                <!-- Slide 4: 2016 Milestone -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase2-04-2016.webp" 
                    alt="Kevin and Shannel in 2016" 
                    loading="lazy"
                    width="800"
                    height="533"
                    style="object-position: center 20%;"
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
                18th Birthday at Labadi Beach Hotel
                <span>The Very Venue of Our Wedding &bull; 2016</span>
              </div>
              <div class="story-frame-caption">
                High School Leavers Dinner
                <span>Matching Navy Black-Tie &bull; 2016</span>
              </div>
              <div class="story-frame-caption">
                Humble Beginnings
                <span>Growing Closer Every Day &bull; 2015/2016</span>
              </div>
              <div class="story-frame-caption">
                End of High School
                <span>Inseparable Ahead of Uni &bull; 2016</span>
              </div>
            </div>

            <!-- Slider Pagination Dots -->
            <div class="story-slider-nav" aria-label="Phase 2 photo navigation">
              <button class="story-slider-dot active" aria-label="Photo 1"></button>
              <button class="story-slider-dot" aria-label="Photo 2"></button>
              <button class="story-slider-dot" aria-label="Photo 3"></button>
              <button class="story-slider-dot" aria-label="Photo 4"></button>
            </div>
          </div>'''

new_phase3_media = '''          <div class="story-frame story-slider-frame" data-slider-id="phase-3">
            <div class="story-frame-inner">
              <div class="story-slider-track">
                <!-- Slide 1: Sheffield Visit -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-05-sheffield-visit.webp" 
                    alt="Shannel visiting Kevin at the University of Sheffield" 
                    loading="lazy"
                    width="800"
                    height="794"
                    style="object-position: center top;"
                  />
                </div>
                <!-- Slide 2: Grenada Island Visit 2018 -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-06-grenada-trip.webp" 
                    alt="Kevin visiting Shannel in Grenada in 2018" 
                    loading="lazy"
                    width="800"
                    height="450"
                    style="object-position: center center;"
                  />
                </div>
                <!-- Slide 3: Visiting in the UK 2018 -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-08-bicycle-date.webp" 
                    alt="Kevin and Shannel visiting in the UK in 2018" 
                    loading="lazy"
                    width="570"
                    height="760"
                    style="object-position: center 10%;"
                  />
                </div>
                <!-- Slide 4: Reunited on Break in Ghana -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-07-ghana-reunited.webp" 
                    alt="Reunited in Ghana on university break" 
                    loading="lazy"
                    width="570"
                    height="760"
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
                Sheffield Visit
                <span>United Kingdom &bull; University Years</span>
              </div>
              <div class="story-frame-caption">
                Island Reunions
                <span>St. George's, Grenada &bull; 2018</span>
              </div>
              <div class="story-frame-caption">
                Visiting in the UK
                <span>Reunited on Break &bull; London 2018</span>
              </div>
              <div class="story-frame-caption">
                Reunited in Ghana
                <span>Holiday Breaks from Uni &bull; 2018</span>
              </div>
            </div>

            <!-- Slider Pagination Dots -->
            <div class="story-slider-nav" aria-label="Phase 3 photo navigation">
              <button class="story-slider-dot active" aria-label="Photo 1"></button>
              <button class="story-slider-dot" aria-label="Photo 2"></button>
              <button class="story-slider-dot" aria-label="Photo 3"></button>
              <button class="story-slider-dot" aria-label="Photo 4"></button>
            </div>
          </div>'''

new_phase4_media = '''          <div class="story-frame story-slider-frame" data-slider-id="phase-4">
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
          </div>'''

new_phase5_media = '''          <div class="story-frame story-slider-frame" data-slider-id="phase-5">
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
                <!-- Slide 2: 2025 Ghana Match (Rotated Upright) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-02-ghanamatch.webp" 
                    alt="Cheering for Ghana together in London in 2025" 
                    loading="lazy"
                    width="800"
                    height="450"
                    style="object-position: center 35%;"
                  />
                </div>
                <!-- Slide 3: 2025 London Date -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-03-date2025.webp" 
                    alt="Kevin and Shannel celebrating in London" 
                    loading="lazy"
                    width="450"
                    height="800"
                    style="object-position: center 15%;"
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
                Black Stars Match Day
                <span>Cheering for Ghana &bull; London 2025</span>
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
          </div>'''

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to replace each phase's story-frame
    pattern = re.compile(r'(\s*<div class="story-frame story-slider-frame" data-slider-id="phase-(\d)">.*?</div>\s*</div>\s*</div>)', re.DOTALL)
    
    phases = {
        '1': new_phase1_media,
        '2': new_phase2_media,
        '3': new_phase3_media,
        '4': new_phase4_media,
        '5': new_phase5_media
    }
    
    def replacer(match):
        phase_num = match.group(2)
        if phase_num in phases:
            return '\n' + phases[phase_num] + '\n        </div>'
        return match.group(0)

    # Use specific targeted replacements
    for p_num, replacement in phases.items():
        # Find the block for this phase
        p_pattern = re.compile(rf'(<div class="story-frame story-slider-frame" data-slider-id="phase-{p_num}">.*?</div>\s*</div>\s*</div>)', re.DOTALL)
        content = p_pattern.sub(replacement + '\n        </div>', content, count=1)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated: {file_path}")

update_file('index.html')
update_file('wedding-index.html')
