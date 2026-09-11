"""
Apply User Feedback Fixes:
1. Update visiting in UK caption in Phase 3 to Christmas break in Ghana 2017.
2. Replace Ghana match day image in Phase 5 with epic shot.webp.
3. Add IMG_0809.webp (Shannel hand ring smile) to #gallery editorial photos.
4. Update London nights photo framing and dimensions in Phase 5 Slide 3.
5. Update High school beach days framing and dimensions in Phase 1 Slide 4.
6. Swap Phase 2 Slide 4 (end of high school) with humble beginnings 3 (story-phase2-04-humble3.webp).
7. Swap Phase 3 Slide 2 (island reunions) with grenada 2 (story-phase3-03-grenada.webp).
8. Ensure 100% parity between index.html and wedding-index.html.
"""
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Phase 1 Slide 4: Beach trip
p1_s4_old = """                <!-- Slide 4: Beach Trip -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-02-beach-trip.webp" 
                    alt="High school beach trip with classmates" 
                    loading="lazy"
                    width="800"
                    height="532"
                    style="object-position: center center;"
                  />
                </div>"""

p1_s4_new = """                <!-- Slide 4: Beach Trip -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-02-beach-trip.webp" 
                    alt="Kevin and Shannel at the high school beach trip in 2015" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>"""

assert p1_s4_old in content, "Phase 1 Slide 4 not found"
content = content.replace(p1_s4_old, p1_s4_new, 1)

# 2. Phase 2 Slide 4: End of High school -> Humble Beginnings 3
p2_s4_old = """                <!-- Slide 4: 2016 Milestone -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase2-04-2016.webp" 
                    alt="Kevin and Shannel in 2016" 
                    loading="lazy"
                    width="800"
                    height="533"
                    style="object-position: center 20%;"
                  />
                </div>"""

p2_s4_new = """                <!-- Slide 4: Humble Beginnings 3 -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase2-04-humble3.webp" 
                    alt="Kevin and Shannel sharing a warm embrace in 2016" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>"""

assert p2_s4_old in content, "Phase 2 Slide 4 not found"
content = content.replace(p2_s4_old, p2_s4_new, 1)

# Phase 2 Caption 4
p2_cap_old = """              <div class="story-frame-caption">
                End of High School
                <span>Inseparable Ahead of Uni &bull; 2016</span>
              </div>"""

p2_cap_new = """              <div class="story-frame-caption">
                Humble Beginnings
                <span>Cherished Moments &bull; 2016</span>
              </div>"""

assert p2_cap_old in content, "Phase 2 Caption 4 not found"
content = content.replace(p2_cap_old, p2_cap_new, 1)

# 3. Phase 3 Slide 2: Grenada Trip -> Grenada 2
p3_s2_old = """                <!-- Slide 2: Grenada Island Visit 2018 -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-06-grenada-trip.webp" 
                    alt="Kevin visiting Shannel in Grenada in 2018" 
                    loading="lazy"
                    width="800"
                    height="450"
                    style="object-position: center center;"
                  />
                </div>"""

p3_s2_new = """                <!-- Slide 2: Grenada Island Visit 2018 -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase3-03-grenada.webp" 
                    alt="Kevin visiting Shannel at the brewery in Grenada in 2018" 
                    loading="lazy"
                    width="450"
                    height="800"
                    style="object-position: center 20%;"
                  />
                </div>"""

assert p3_s2_old in content, "Phase 3 Slide 2 not found"
content = content.replace(p3_s2_old, p3_s2_new, 1)

# 4. Phase 3 Slide 3: Visiting in UK caption -> Christmas Break in Ghana 2017
p3_s3_old = """                <!-- Slide 3: Visiting in the UK 2018 -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-08-bicycle-date.webp" 
                    alt="Kevin and Shannel visiting in the UK in 2018" 
                    loading="lazy"
                    width="570"
                    height="760"
                    style="object-position: center 10%;"
                  />
                </div>"""

p3_s3_new = """                <!-- Slide 3: Christmas Break in Ghana 2017 -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-08-bicycle-date.webp" 
                    alt="Kevin and Shannel during Christmas break in Ghana in 2017" 
                    loading="lazy"
                    width="570"
                    height="760"
                    style="object-position: center 10%;"
                  />
                </div>"""

assert p3_s3_old in content, "Phase 3 Slide 3 not found"
content = content.replace(p3_s3_old, p3_s3_new, 1)

p3_cap_old = """              <div class="story-frame-caption">
                Visiting in the UK
                <span>Reunited on Break &bull; London 2018</span>
              </div>"""

p3_cap_new = """              <div class="story-frame-caption">
                Christmas Break in Ghana
                <span>Holiday Break from Uni &bull; 2017</span>
              </div>"""

assert p3_cap_old in content, "Phase 3 Caption 3 not found"
content = content.replace(p3_cap_old, p3_cap_new, 1)

# 5. Phase 5 Slide 2: Replace Ghana Match with Epic Shot
p5_s2_old = """                <!-- Slide 2: 2025 Ghana Match (Rotated Upright) -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-02-ghanamatch.webp" 
                    alt="Cheering for Ghana together in London in 2025" 
                    loading="lazy"
                    width="800"
                    height="450"
                    style="object-position: center 35%;"
                  />
                </div>"""

p5_s2_new = """                <!-- Slide 2: An Epic Proposal 2025 -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-02-epicshot.webp" 
                    alt="Kevin and Shannel embracing on their engagement proposal night in London" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>"""

assert p5_s2_old in content, "Phase 5 Slide 2 not found"
content = content.replace(p5_s2_old, p5_s2_new, 1)

p5_cap_old = """              <div class="story-frame-caption">
                Black Stars Match Day
                <span>Cheering for Ghana &bull; London 2025</span>
              </div>"""

p5_cap_new = """              <div class="story-frame-caption">
                An Epic Proposal
                <span>London City Nights &bull; 2025</span>
              </div>"""

assert p5_cap_old in content, "Phase 5 Caption 2 not found"
content = content.replace(p5_cap_old, p5_cap_new, 1)

# 6. Phase 5 Slide 3: London Nights framing
p5_s3_old = """                <!-- Slide 3: 2025 London Date -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-03-date2025.webp" 
                    alt="Kevin and Shannel celebrating in London" 
                    loading="lazy"
                    width="450"
                    height="800"
                    style="object-position: center 15%;"
                  />
                </div>"""

p5_s3_new = """                <!-- Slide 3: 2025 London Date -->
                <div class="story-slide">
                  <img 
                    src="assets/images/story/story-phase5-03-date2025.webp" 
                    alt="Kevin and Shannel celebrating in London" 
                    loading="lazy"
                    width="720"
                    height="810"
                    style="object-position: center center;"
                  />
                </div>"""

assert p5_s3_old in content, "Phase 5 Slide 3 not found"
content = content.replace(p5_s3_old, p5_s3_new, 1)

# 7. Editorial Photos Grid: Add IMG_0809.webp
gallery_old = """      <!-- Photo 3: Bouquet & Engagement Ring -->
      <div class="gallery-item" data-category="details">
        <img src="assets/images/IMG_0864.webp" alt="Appleyard London red rose bouquet and sparkling diamond ring" loading="lazy" />
        <div class="gallery-overlay">
          <div class="gallery-overlay-text">
            <h4>Appleyard Roses & Diamond</h4>
            <span>Details</span>
          </div>
        </div>
      </div>"""

gallery_new = """      <!-- Photo 3: Bouquet & Engagement Ring -->
      <div class="gallery-item" data-category="details">
        <img src="assets/images/IMG_0864.webp" alt="Appleyard London red rose bouquet and sparkling diamond ring" loading="lazy" />
        <div class="gallery-overlay">
          <div class="gallery-overlay-text">
            <h4>Appleyard Roses & Diamond</h4>
            <span>Details</span>
          </div>
        </div>
      </div>

      <!-- Photo: Hand with Ring & Radiant Smile -->
      <div class="gallery-item" data-category="details twilight portraits">
        <img src="assets/images/IMG_0809.webp" alt="Shannel holding out her hand showcasing engagement ring with a radiant smile" loading="lazy" />
        <div class="gallery-overlay">
          <div class="gallery-overlay-text">
            <h4>The Ring &amp; The Smile</h4>
            <span>Editorial Details</span>
          </div>
        </div>
      </div>"""

assert gallery_old in content, "Gallery anchor not found"
content = content.replace(gallery_old, gallery_new, 1)

# Write updated content to index.html and wedding-index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("wedding-index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully updated index.html and wedding-index.html with 100% parity!")
