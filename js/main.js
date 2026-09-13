/**
 * Kevin & Shannel — Wedding Celebration
 * Saturday, 9th January 2027 | Labadi Beach Hotel, Accra, Ghana
 * Master JavaScript Logic
 */

document.addEventListener("DOMContentLoaded", () => {
  /* ==========================================================================
     CONFIGURATION SETTINGS (Easily updated by the couple)
     ========================================================================== */
  const CONFIG = {
    // Guest Access Password
    password: "FOREVER2027",
    
    // Wedding Date & Time (January 9, 2027, 1:00 PM GMT Accra)
    weddingDate: new Date("January 9, 2027 13:00:00 GMT").getTime(),
    
    // WithJoy.com URLs
    joyRegistryUrl: "https://withjoy.com/kevin-and-shannel/registry",
    joySiteUrl: "https://withjoy.com/kevin-and-shannel",

    // Google Sheets Webhook URL for real-time private RSVP collection (Optional)
    rsvpWebhookUrl: "",
    
    // Event Details for Calendar Invites
    event: {
      title: "Kevin & Shannel's Wedding Celebration",
      description: "Join us in celebrating the White Wedding of Kevin & Shannel at the Labadi Beach Hotel in Accra, Ghana.",
      location: "Labadi Beach Hotel, No 1 La Bypass, Accra, Ghana",
      startDate: "20270109T130000Z",
      endDate: "20270109T230000Z"
    }
  };

  /* ==========================================================================
     1. BESPOKE LUXURY PASSWORD GATE (SINGLE-PHASE ENTRY)
     ========================================================================== */
  const gate = document.getElementById("passwordGate");
  const gateForm = document.getElementById("gateForm");
  const gatePassword = document.getElementById("gatePassword");
  const gateError = document.getElementById("gateError");
  const gateCard = document.getElementById("gateCard");

  // Check if session is already authenticated
  if (sessionStorage.getItem("wedding_unlocked") === "true") {
    gate.classList.add("unlocked");
  }

  function unlockGate() {
    if (gateError) gateError.style.display = "none";
    sessionStorage.setItem("wedding_unlocked", "true");
    gate.classList.add("unlocked");
  }

  if (gateForm) {
    gateForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const entered = gatePassword.value.trim();
      if (entered.toUpperCase() === CONFIG.password.toUpperCase()) {
        unlockGate();
      } else {
        if (gateCard) {
          gateCard.classList.add("lock-error-shake");
          setTimeout(() => gateCard.classList.remove("lock-error-shake"), 500);
        }
        if (gateError) gateError.style.display = "block";
        gatePassword.value = "";
        gatePassword.focus();
      }
    });
  }

  // Developer / Couple helper to re-lock and preview the gate anytime
  window.openPasswordGate = function () {
    sessionStorage.removeItem("wedding_unlocked");
    gate.classList.remove("unlocked");
    if (gateCard) gateCard.classList.remove("lock-error-shake");
    if (gatePassword) {
      gatePassword.value = "";
      gatePassword.focus();
    }
    if (gateError) gateError.style.display = "none";
  };

  /* ==========================================================================
     2. NAVIGATION & MOBILE DRAWER
     ========================================================================== */
  const nav = document.querySelector("nav");
  const hamburger = document.getElementById("navHamburger");
  const mobileDrawer = document.getElementById("mobileDrawer");
  const mobileBackdrop = document.getElementById("mobileBackdrop");
  const navLinks = document.querySelectorAll(".nav-links a, .mobile-nav-links a");

  // Dynamic Scroll Glassmorphism
  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      nav.classList.add("scrolled");
    } else {
      nav.classList.remove("scrolled");
    }
  });

  // Mobile Drawer Toggle
  function toggleMobileMenu(open) {
    const isOpen = open !== undefined ? open : !mobileDrawer.classList.contains("open");
    if (isOpen) {
      mobileDrawer.classList.add("open");
      mobileBackdrop.classList.add("open");
      hamburger.classList.add("active");
      document.body.style.overflow = "hidden";
    } else {
      mobileDrawer.classList.remove("open");
      mobileBackdrop.classList.remove("open");
      hamburger.classList.remove("active");
      document.body.style.overflow = "";
    }
  }

  if (hamburger) {
    hamburger.addEventListener("click", () => toggleMobileMenu());
  }
  if (mobileBackdrop) {
    mobileBackdrop.addEventListener("click", () => toggleMobileMenu(false));
  }

  // Close mobile drawer upon link click
  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      toggleMobileMenu(false);
    });
  });

  // Active section indicator on scroll
  const sections = document.querySelectorAll("section[id]");
  const observerNav = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute("id");
          document.querySelectorAll(".nav-links a").forEach((a) => {
            a.classList.toggle("active", a.getAttribute("href") === `#${id}`);
          });
        }
      });
    },
    { threshold: 0.3 }
  );
  sections.forEach((sec) => observerNav.observe(sec));

  /* ==========================================================================
     3. LIVE COUNTDOWN TIMER
     ========================================================================== */
  const daysEl = document.getElementById("days");
  const hoursEl = document.getElementById("hours");
  const minsEl = document.getElementById("minutes");
  const secsEl = document.getElementById("seconds");

  function updateCountdown() {
    const now = new Date().getTime();
    const distance = CONFIG.weddingDate - now;

    if (distance > 0) {
      const days = Math.floor(distance / (1000 * 60 * 60 * 24));
      const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((distance % (1000 * 60)) / 1000);

      if (daysEl) daysEl.innerText = String(days).padStart(2, "0");
      if (hoursEl) hoursEl.innerText = String(hours).padStart(2, "0");
      if (minsEl) minsEl.innerText = String(minutes).padStart(2, "0");
      if (secsEl) secsEl.innerText = String(seconds).padStart(2, "0");
    } else {
      const timerContainer = document.querySelector(".timer-container");
      if (timerContainer) {
        timerContainer.innerHTML = `<div class="badge-gold" style="font-size:1.1rem; padding: 12px 24px;">Today We Celebrate!</div>`;
      }
    }
  }

  setInterval(updateCountdown, 1000);
  updateCountdown();

  /* ==========================================================================
     4. SAVE TO CALENDAR (Google Calendar & .ICS Download)
     ========================================================================== */
  const calendarDropdown = document.getElementById("calendarDropdown");
  const calendarToggleBtn = document.getElementById("calendarToggleBtn");
  const googleCalLink = document.getElementById("googleCalLink");
  const appleCalLink = document.getElementById("appleCalLink");

  if (calendarToggleBtn && calendarDropdown) {
    calendarToggleBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      calendarDropdown.classList.toggle("open");
    });

    document.addEventListener("click", (e) => {
      if (!calendarDropdown.contains(e.target)) {
        calendarDropdown.classList.remove("open");
      }
    });
  }

  // Google Calendar URL
  if (googleCalLink) {
    const gCalUrl = `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${encodeURIComponent(
      CONFIG.event.title
    )}&dates=${CONFIG.event.startDate}/${CONFIG.event.endDate}&details=${encodeURIComponent(
      CONFIG.event.description
    )}&location=${encodeURIComponent(CONFIG.event.location)}`;
    googleCalLink.setAttribute("href", gCalUrl);
  }

  // Apple / Outlook .ICS Generator & Download
  if (appleCalLink) {
    appleCalLink.addEventListener("click", (e) => {
      e.preventDefault();
      const icsContent = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Kevin and Shannel Wedding//EN",
        "CALSCALE:GREGORIAN",
        "BEGIN:VEVENT",
        `SUMMARY:${CONFIG.event.title}`,
        `DESCRIPTION:${CONFIG.event.description}`,
        `LOCATION:${CONFIG.event.location}`,
        `DTSTART:${CONFIG.event.startDate}`,
        `DTEND:${CONFIG.event.endDate}`,
        "STATUS:CONFIRMED",
        "END:VEVENT",
        "END:VCALENDAR"
      ].join("\r\n");

      const blob = new Blob([icsContent], { type: "text/calendar;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const tempLink = document.createElement("a");
      tempLink.href = url;
      tempLink.setAttribute("download", "Kevin-and-Shannel-Wedding.ics");
      document.body.appendChild(tempLink);
      tempLink.click();
      document.body.removeChild(tempLink);
      URL.revokeObjectURL(url);
    });
  }

  /* ==========================================================================
     5. SCROLL REVEAL ANIMATIONS
     ========================================================================== */
  const revealElements = document.querySelectorAll(".reveal-on-scroll");
  const revealObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-revealed");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.02, rootMargin: "0px 0px -20px 0px" }
  );

  revealElements.forEach((el) => revealObserver.observe(el));

  /* ==========================================================================
     6. EDITORIAL PHOTO GALLERY & LIGHTBOX
     ========================================================================== */
  const galleryItems = document.querySelectorAll(".gallery-item");
  const filterBtns = document.querySelectorAll(".gallery-filter-btn");
  const lightbox = document.getElementById("galleryLightbox");
  const lightboxImg = document.getElementById("lightboxImg");
  const lightboxClose = document.getElementById("lightboxClose");
  const lightboxPrev = document.getElementById("lightboxPrev");
  const lightboxNext = document.getElementById("lightboxNext");

  let currentGalleryIndex = 0;
  let activeGalleryList = [];

  function updateActiveList() {
    activeGalleryList = Array.from(galleryItems).filter(
      (item) => item.style.display !== "none"
    );
  }
  updateActiveList();

  // Category Filtering
  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterBtns.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");

      const category = btn.getAttribute("data-filter");
      galleryItems.forEach((item) => {
        const itemCat = item.getAttribute("data-category");
        if (category === "all" || itemCat.includes(category)) {
          item.style.display = "";
        } else {
          item.style.display = "none";
        }
      });
      updateActiveList();
    });
  });

  // Open Lightbox
  function openLightbox(index) {
    if (activeGalleryList.length === 0) return;
    currentGalleryIndex = (index + activeGalleryList.length) % activeGalleryList.length;
    const targetItem = activeGalleryList[currentGalleryIndex];
    const imgSrc = targetItem.querySelector("img").getAttribute("src");
    lightboxImg.src = imgSrc;
    lightbox.classList.add("active");
    document.body.style.overflow = "hidden";
  }

  function closeLightbox() {
    lightbox.classList.remove("active");
    document.body.style.overflow = "";
  }

  galleryItems.forEach((item) => {
    item.addEventListener("click", () => {
      const idx = activeGalleryList.indexOf(item);
      if (idx !== -1) openLightbox(idx);
    });
  });

  if (lightboxClose) lightboxClose.addEventListener("click", closeLightbox);
  if (lightboxPrev) {
    lightboxPrev.addEventListener("click", (e) => {
      e.stopPropagation();
      openLightbox(currentGalleryIndex - 1);
    });
  }
  if (lightboxNext) {
    lightboxNext.addEventListener("click", (e) => {
      e.stopPropagation();
      openLightbox(currentGalleryIndex + 1);
    });
  }

  // Close on backdrop click
  if (lightbox) {
    lightbox.addEventListener("click", (e) => {
      if (e.target === lightbox) closeLightbox();
    });
  }

  // Keyboard navigation for Lightbox
  document.addEventListener("keydown", (e) => {
    if (!lightbox || !lightbox.classList.contains("active")) return;
    if (e.key === "Escape") closeLightbox();
    if (e.key === "ArrowLeft") openLightbox(currentGalleryIndex - 1);
    if (e.key === "ArrowRight") openLightbox(currentGalleryIndex + 1);
  });

  /* ==========================================================================
     7. WITHJOY REGISTRY MODAL & DIRECT LINKS
     ========================================================================== */
  const joyModal = document.getElementById("joyModal");
  const openJoyBtns = document.querySelectorAll(".open-joy-modal-btn");
  const joyModalClose = document.getElementById("joyModalClose");
  const joyModalDismiss = document.getElementById("joyModalDismiss");
  const joyDirectLink = document.getElementById("joyDirectLink");
  const joyPrimaryBtn = document.getElementById("joyPrimaryBtn");

  if (joyDirectLink) {
    joyDirectLink.setAttribute("href", CONFIG.joySiteUrl);
  }
  if (joyPrimaryBtn) {
    joyPrimaryBtn.setAttribute("href", CONFIG.joyRegistryUrl);
  }

  function openJoyModal() {
    if (!joyModal) return;
    joyModal.classList.add("active");
    document.body.style.overflow = "hidden";
  }

  function closeJoyModal() {
    if (!joyModal) return;
    joyModal.classList.remove("active");
    document.body.style.overflow = "";
  }

  openJoyBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      openJoyModal();
    });
  });

  if (joyModalClose) joyModalClose.addEventListener("click", closeJoyModal);
  if (joyModalDismiss) joyModalDismiss.addEventListener("click", closeJoyModal);
  if (joyModal) {
    joyModal.addEventListener("click", (e) => {
      if (e.target === joyModal) closeJoyModal();
    });
  }

  /* ==========================================================================
     8. BANK DETAILS & MOBILE MONEY (MOMO) MODAL
     ========================================================================== */
  const bankModal = document.getElementById("bankModal");
  const openBankBtns = document.querySelectorAll(".open-bank-modal-btn");
  const bankModalClose = document.getElementById("bankModalClose");

  function openBankModal() {
    if (!bankModal) return;
    bankModal.classList.add("active");
    document.body.style.overflow = "hidden";
  }

  function closeBankModal() {
    if (!bankModal) return;
    bankModal.classList.remove("active");
    document.body.style.overflow = "";
  }

  openBankBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      openBankModal();
    });
  });

  if (bankModalClose) bankModalClose.addEventListener("click", closeBankModal);
  if (bankModal) {
    bankModal.addEventListener("click", (e) => {
      if (e.target === bankModal) closeBankModal();
    });
  }

  /* ==========================================================================
     9. TIERED INVITE-ONLY RSVP & PASSCODE GATE
     ========================================================================== */
  // Master Invitations Registry with Tier Limits & Privileges
  const RSVP_INVITATIONS = {
    // --- Solo Guest Passes (Strictly 1 Seat) ---
    "SOLO27": { tier: "solo", maxGuests: 1, label: "Single Guest Invitation", guest: "" },
    "KS-SOLO": { tier: "solo", maxGuests: 1, label: "Single Guest Invitation", guest: "" },

    // --- Plus-One Guest Passes (Up to 2 Seats) ---
    "PLUS1": { tier: "plus-one", maxGuests: 2, label: "Guest & Plus-One Invitation", guest: "" },
    "COUPLE27": { tier: "plus-one", maxGuests: 2, label: "Couple Invitation", guest: "" },
    "KS-PLUSONE": { tier: "plus-one", maxGuests: 2, label: "Guest & Plus-One Invitation", guest: "" },

    // --- Family & Group Delegations (Up to 4-5 Seats) ---
    "FAMILY27": { tier: "family", maxGuests: 4, label: "Family Delegation (Up to 4)", guest: "" },
    "MENSAH-FAM": { tier: "family", maxGuests: 4, label: "Mensah Family Delegation", guest: "Mensah Family" },
    "QUAYE-FAM": { tier: "family", maxGuests: 4, label: "Quaye Family Delegation", guest: "Quaye Family" },
    "VIP-DELEGATION": { tier: "family", maxGuests: 5, label: "Special Family / Group Delegation", guest: "" },

    // --- Bride & Groom Mastercodes (Exempt from single-use lock, flexible party up to 10) ---
    "FOREVER2027": { tier: "family", maxGuests: 10, label: "Bride & Groom Master Pass", guest: "Kevin & Shannel", isMaster: true },
    "KS-VIP": { tier: "family", maxGuests: 10, label: "Bride & Groom VIP Pass", guest: "Kevin & Shannel", isMaster: true },
    "KS-MASTER": { tier: "family", maxGuests: 10, label: "Bride & Groom Master Pass", guest: "Kevin & Shannel", isMaster: true }
  };

  const rsvpPasscodeBlock = document.getElementById("rsvpPasscodeBlock");
  const rsvpCodeInput = document.getElementById("rsvpCodeInput");
  const verifyRsvpCodeBtn = document.getElementById("verifyRsvpCodeBtn");
  const rsvpStatusMsg = document.getElementById("rsvpStatusMsg");

  const rsvpForm = document.getElementById("rsvpForm");
  const verifiedCodeInput = document.getElementById("verifiedCode");
  const verifiedTierInput = document.getElementById("verifiedTier");
  const fullNameInput = document.getElementById("fullName");
  const partySizeContainer = document.getElementById("partySizeContainer");
  const accompanyingNamesGroup = document.getElementById("accompanyingNamesGroup");
  const accompanyingNamesLabel = document.getElementById("accompanyingNamesLabel");
  const accompanyingNamesInput = document.getElementById("accompanyingNames");
  const accompanyingNamesHelp = document.getElementById("accompanyingNamesHelp");

  const rsvpSuccess = document.getElementById("rsvpSuccess");
  const rsvpConfirmationSummary = document.getElementById("rsvpConfirmationSummary");
  const resetRsvpBtn = document.getElementById("resetRsvpBtn");

  function showRsvpStatus(type, html) {
    if (!rsvpStatusMsg) return;
    rsvpStatusMsg.className = `rsvp-status-msg ${type}`;
    rsvpStatusMsg.innerHTML = html;
    rsvpStatusMsg.style.display = "block";
  }

  function configureTierUI(inv) {
    if (!partySizeContainer) return;

    if (inv.tier === "solo") {
      partySizeContainer.innerHTML = `
        <label for="guestCount">Total Number in Party</label>
        <div class="rsvp-party-locked-note">
          <span><strong>1 Reserved Seat</strong> (Individual Guest)</span>
          <span class="rsvp-party-locked-tag">Solo Pass</span>
        </div>
        <input type="hidden" id="guestCount" name="guestCount" value="1" />
      `;
      if (accompanyingNamesGroup) {
        accompanyingNamesGroup.classList.remove("active");
        if (accompanyingNamesInput) {
          accompanyingNamesInput.removeAttribute("required");
          accompanyingNamesInput.value = "";
        }
      }
    } else if (inv.tier === "plus-one") {
      partySizeContainer.innerHTML = `
        <label for="guestCount">Total Number in Party</label>
        <select id="guestCount" required>
          <option value="1">1 Guest (Attending Solo)</option>
          <option value="2" selected>2 Guests (Attending with +1)</option>
        </select>
      `;
      if (accompanyingNamesLabel) accompanyingNamesLabel.textContent = "Accompanying Guest Full Name";
      if (accompanyingNamesInput) {
        accompanyingNamesInput.placeholder = "e.g. Ama Boateng";
      }
      if (accompanyingNamesHelp) {
        accompanyingNamesHelp.textContent = "Please provide the full legal name of your accompanying guest for the guest list.";
      }

      const countSelect = document.getElementById("guestCount");
      function updatePlusOneField() {
        if (!countSelect || !accompanyingNamesGroup) return;
        if (countSelect.value === "2") {
          accompanyingNamesGroup.classList.add("active");
          if (accompanyingNamesInput) accompanyingNamesInput.setAttribute("required", "required");
        } else {
          accompanyingNamesGroup.classList.remove("active");
          if (accompanyingNamesInput) {
            accompanyingNamesInput.removeAttribute("required");
            accompanyingNamesInput.value = "";
          }
        }
      }
      if (countSelect) {
        countSelect.addEventListener("change", updatePlusOneField);
        updatePlusOneField();
      }
    } else if (inv.tier === "family") {
      let optionsHtml = "";
      for (let i = 1; i <= inv.maxGuests; i++) {
        const sel = (i === inv.maxGuests) ? "selected" : "";
        optionsHtml += `<option value="${i}" ${sel}>${i} ${i === 1 ? "Guest" : "Guests in Family Party"}</option>`;
      }
      partySizeContainer.innerHTML = `
        <label for="guestCount">Total Number in Party</label>
        <select id="guestCount" required>${optionsHtml}</select>
      `;
      if (accompanyingNamesLabel) accompanyingNamesLabel.textContent = "Accompanying Family / Children Names";
      if (accompanyingNamesInput) {
        accompanyingNamesInput.placeholder = "e.g. Ama Mensah, Kofi Mensah (Age 8)";
      }
      if (accompanyingNamesHelp) {
        accompanyingNamesHelp.textContent = "Please list full names of all accompanying family members and children.";
      }

      const countSelect = document.getElementById("guestCount");
      function updateFamilyField() {
        if (!countSelect || !accompanyingNamesGroup) return;
        const val = parseInt(countSelect.value, 10);
        if (val > 1) {
          accompanyingNamesGroup.classList.add("active");
          if (accompanyingNamesInput) accompanyingNamesInput.setAttribute("required", "required");
        } else {
          accompanyingNamesGroup.classList.remove("active");
          if (accompanyingNamesInput) {
            accompanyingNamesInput.removeAttribute("required");
            accompanyingNamesInput.value = "";
          }
        }
      }
      if (countSelect) {
        countSelect.addEventListener("change", updateFamilyField);
        updateFamilyField();
      }
    }
  }

  function handlePasscodeVerification() {
    if (!rsvpCodeInput) return;
    const code = rsvpCodeInput.value.trim().toUpperCase();

    if (!code) {
      showRsvpStatus("warning", "Please enter your invitation passcode before verifying.");
      return;
    }

    // Check validity in invitation registry
    const inv = RSVP_INVITATIONS[code];
    if (!inv) {
      showRsvpStatus("error", `
        We could not find an invitation associated with code "<strong>${code}</strong>".<br>
        <span style="font-size: 0.82rem; margin-top: 4px; display: inline-block;">
          Please check the passcode on your invitation card or message, or reach out to the couple.
        </span>
      `);
      if (rsvpPasscodeBlock) rsvpPasscodeBlock.classList.remove("verified");
      if (rsvpForm) rsvpForm.classList.remove("active");
      return;
    }

    // Check single-use redemption history (Mastercodes are exempt)
    if (!inv.isMaster) {
      let redeemed = {};
      try {
        redeemed = JSON.parse(localStorage.getItem("wedding_redeemed_codes") || "{}");
      } catch (e) {
        redeemed = {};
      }

      if (redeemed[code]) {
        const rec = redeemed[code];
        showRsvpStatus("warning", `
          This invitation code (<strong>${code}</strong>) was already registered on ${rec.date || "a previous date"} for <strong>${rec.fullName || "a guest"}</strong>.<br>
          <span style="font-size: 0.82rem; margin-top: 6px; display: inline-block;">
            If you need to make changes to your registered party, please contact Kevin &amp; Shannel directly.
          </span>
        `);
        if (rsvpPasscodeBlock) rsvpPasscodeBlock.classList.remove("verified");
        if (rsvpForm) rsvpForm.classList.remove("active");
        return;
      }
    }

    // Success: Unlock form and set up tier
    if (rsvpPasscodeBlock) rsvpPasscodeBlock.classList.add("verified");
    if (verifiedCodeInput) verifiedCodeInput.value = code;
    if (verifiedTierInput) verifiedTierInput.value = inv.tier;

    showRsvpStatus("success", `
      <div style="font-weight: 600; font-size: 0.95rem; margin-bottom: 4px;">Invitation Verified ✓</div>
      <div>Welcome to the celebration! Your RSVP has been unlocked.</div>
      <div class="rsvp-tier-pill">${inv.label}</div>
    `);

    configureTierUI(inv);

    if (inv.guest && fullNameInput && !fullNameInput.value.trim()) {
      fullNameInput.value = inv.guest;
    }

    if (rsvpForm) {
      rsvpForm.classList.add("active");
      rsvpForm.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  if (verifyRsvpCodeBtn) {
    verifyRsvpCodeBtn.addEventListener("click", handlePasscodeVerification);
  }

  if (rsvpCodeInput) {
    rsvpCodeInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        e.preventDefault();
        handlePasscodeVerification();
      }
    });
  }

  if (rsvpForm) {
    rsvpForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const code = (verifiedCodeInput ? verifiedCodeInput.value : "").trim().toUpperCase();
      const tier = (verifiedTierInput ? verifiedTierInput.value : "") || "solo";

      if (!code) {
        alert("Please enter and verify your invitation passcode first.");
        if (rsvpPasscodeBlock) rsvpPasscodeBlock.scrollIntoView({ behavior: "smooth", block: "center" });
        return;
      }

      const guestCountEl = document.getElementById("guestCount");
      const guestCountVal = guestCountEl ? guestCountEl.value : "1";
      const accompanyingVal = accompanyingNamesInput ? accompanyingNamesInput.value.trim() : "";

      const rsvpData = {
        timestamp: new Date().toISOString(),
        passcode: code,
        tier: tier,
        fullName: fullNameInput ? fullNameInput.value.trim() : "",
        email: document.getElementById("email")?.value.trim() || "",
        phone: document.getElementById("phone")?.value.trim() || "",
        attendance: document.getElementById("ceremonies")?.value || "",
        guestCount: guestCountVal,
        accompanyingNames: accompanyingVal,
        dietary: document.getElementById("dietary")?.value.trim() || "None",
        message: document.getElementById("message")?.value.trim() || ""
      };

      // Save to localStorage wedding_rsvps
      try {
        const stored = JSON.parse(localStorage.getItem("wedding_rsvps") || "[]");
        stored.push(rsvpData);
        localStorage.setItem("wedding_rsvps", JSON.stringify(stored));
        console.log("RSVP registered successfully:", rsvpData);
      } catch (err) {
        console.error("Local storage error:", err);
      }

      // Record passcode redemption to enforce single-use (Exempt for mastercodes)
      if (!RSVP_INVITATIONS[code]?.isMaster) {
        try {
          const redeemed = JSON.parse(localStorage.getItem("wedding_redeemed_codes") || "{}");
          redeemed[code] = {
            date: new Date().toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" }),
            fullName: rsvpData.fullName,
            guestCount: rsvpData.guestCount,
            attendance: rsvpData.attendance
          };
          localStorage.setItem("wedding_redeemed_codes", JSON.stringify(redeemed));
        } catch (err) {
          console.error("Redemption storage error:", err);
        }
      }

      // Async POST to Google Sheet Webhook if configured
      if (CONFIG.rsvpWebhookUrl) {
        try {
          fetch(CONFIG.rsvpWebhookUrl, {
            method: "POST",
            mode: "no-cors",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(rsvpData)
          }).catch((webhookErr) => {
            console.warn("Google Sheet Webhook background sync note:", webhookErr);
          });
        } catch (postErr) {
          console.warn("Webhook fetch initialization:", postErr);
        }
      }

      // Render confirmation summary
      if (rsvpConfirmationSummary) {
        const invInfo = RSVP_INVITATIONS[code] || { label: "Wedding Invitation" };
        rsvpConfirmationSummary.innerHTML = `
          <div class="rsvp-summary-row">
            <span>Invitation Passcode</span>
            <span>${code} (${invInfo.label})</span>
          </div>
          <div class="rsvp-summary-row">
            <span>Primary Guest</span>
            <span>${rsvpData.fullName}</span>
          </div>
          <div class="rsvp-summary-row">
            <span>Attendance Status</span>
            <span>${rsvpData.attendance}</span>
          </div>
          <div class="rsvp-summary-row">
            <span>Total Party Size</span>
            <span>${rsvpData.guestCount} ${parseInt(rsvpData.guestCount, 10) === 1 ? "Guest" : "Guests"}</span>
          </div>
          ${rsvpData.accompanyingNames ? `
          <div class="rsvp-summary-row">
            <span>Accompanying Guest(s)</span>
            <span>${rsvpData.accompanyingNames}</span>
          </div>` : ""}
          <div class="rsvp-summary-row">
            <span>Contact Details</span>
            <span>${rsvpData.phone} | ${rsvpData.email}</span>
          </div>
        `;
      }

      // Transition to Success state
      if (rsvpPasscodeBlock) rsvpPasscodeBlock.style.display = "none";
      rsvpForm.style.display = "none";
      if (rsvpSuccess) {
        rsvpSuccess.style.display = "block";
        rsvpSuccess.scrollIntoView({ behavior: "smooth", block: "center" });
      }
    });
  }

  if (resetRsvpBtn) {
    resetRsvpBtn.addEventListener("click", () => {
      if (rsvpForm) {
        rsvpForm.reset();
        rsvpForm.classList.remove("active");
        rsvpForm.style.display = "";
      }
      if (rsvpPasscodeBlock) {
        rsvpPasscodeBlock.classList.remove("verified");
        rsvpPasscodeBlock.style.display = "";
      }
      if (rsvpCodeInput) rsvpCodeInput.value = "";
      if (rsvpStatusMsg) {
        rsvpStatusMsg.className = "rsvp-status-msg";
        rsvpStatusMsg.style.display = "none";
        rsvpStatusMsg.innerHTML = "";
      }
      if (accompanyingNamesGroup) {
        accompanyingNamesGroup.classList.remove("active");
      }
      if (rsvpSuccess) rsvpSuccess.style.display = "none";
      if (rsvpPasscodeBlock) {
        rsvpPasscodeBlock.scrollIntoView({ behavior: "smooth", block: "center" });
      }
    });
  }

  // Developer / Couple Helper to export all RSVPs to CSV from console:
  window.exportRSVPs = function () {
    const data = JSON.parse(localStorage.getItem("wedding_rsvps") || "[]");
    if (data.length === 0) {
      alert("No RSVP responses stored yet.");
      return;
    }
    const headers = ["Timestamp", "Passcode", "Tier", "Full Name", "Email", "Phone", "Attendance", "Guests", "Accompanying Guests", "Dietary", "Message"];
    const rows = data.map((d) => [
      `"${d.timestamp || ""}"`,
      `"${d.passcode || ""}"`,
      `"${d.tier || ""}"`,
      `"${(d.fullName || "").replace(/"/g, '""')}"`,
      `"${(d.email || "").replace(/"/g, '""')}"`,
      `"${(d.phone || "").replace(/"/g, '""')}"`,
      `"${(d.attendance || "").replace(/"/g, '""')}"`,
      `"${d.guestCount || "1"}"`,
      `"${(d.accompanyingNames || "").replace(/"/g, '""')}"`,
      `"${(d.dietary || "").replace(/"/g, '""')}"`,
      `"${(d.message || "").replace(/"/g, '""')}"`
    ]);
    const csvContent = "data:text/csv;charset=utf-8," + [headers.join(","), ...rows.map((r) => r.join(","))].join("\n");
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `Kevin_Shannel_RSVPs_${new Date().toISOString().slice(0, 10)}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  // Helper to reset redeemed codes during testing
  window.resetRSVPCodes = function () {
    localStorage.removeItem("wedding_redeemed_codes");
    alert("All invitation passcodes have been reset for testing.");
  };

  /* ==========================================================================
     10. EXPANDABLE FAQ ACCORDION
     ========================================================================== */
  const faqQuestions = document.querySelectorAll(".faq-question");

  faqQuestions.forEach((button) => {
    button.addEventListener("click", () => {
      const item = button.parentElement;
      const isActive = item.classList.contains("active");

      document.querySelectorAll(".faq-item").forEach((other) => {
        other.classList.remove("active");
      });

      if (!isActive) {
        item.classList.add("active");
      }
    });
  });

  /* ==========================================================================
     11. HERO LIVING DYNAMICS (Stardust Particles, Auto-Crossfade & Parallax)
     ========================================================================== */

  // A. Hero Stardust Micro-Particles Engine
  function initHeroStardust() {
    const canvas = document.getElementById("heroStardust");
    const heroSection = document.getElementById("hero");
    if (!canvas || !heroSection) return;

    const ctx = canvas.getContext("2d");
    let animationFrameId = null;
    let isVisible = true;
    let width = 0;
    let height = 0;

    const particles = [];
    const PARTICLE_COUNT = 28;

    function resize() {
      width = canvas.width = heroSection.offsetWidth;
      height = canvas.height = heroSection.offsetHeight;
    }

    window.addEventListener("resize", resize, { passive: true });
    resize();

    class StardustParticle {
      constructor(isInitial = false) {
        this.reset(isInitial);
      }

      reset(isInitial = false) {
        this.x = Math.random() * width;
        this.y = isInitial ? Math.random() * height : height + Math.random() * 20;
        this.radius = 0.6 + Math.random() * 1.3;
        this.speedY = 0.18 + Math.random() * 0.4;
        this.speedX = (Math.random() - 0.5) * 0.22;
        this.alpha = 0.12 + Math.random() * 0.42;
        this.pulseSpeed = 0.012 + Math.random() * 0.02;
        this.pulseVal = Math.random() * Math.PI * 2;
      }

      update() {
        this.y -= this.speedY;
        this.x += this.speedX;
        this.pulseVal += this.pulseSpeed;

        if (this.y < -10 || this.x < -10 || this.x > width + 10) {
          this.reset(false);
        }
      }

      draw() {
        const currentAlpha = Math.max(0.06, this.alpha + Math.sin(this.pulseVal) * 0.18);
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(212, 175, 55, ${currentAlpha})`;
        ctx.shadowBlur = 4;
        ctx.shadowColor = "rgba(212, 175, 55, 0.4)";
        ctx.fill();
        ctx.shadowBlur = 0;
      }
    }

    for (let i = 0; i < PARTICLE_COUNT; i++) {
      particles.push(new StardustParticle(true));
    }

    function loop() {
      if (!isVisible) return;
      ctx.clearRect(0, 0, width, height);

      for (let i = 0; i < particles.length; i++) {
        particles[i].update();
        particles[i].draw();
      }

      animationFrameId = requestAnimationFrame(loop);
    }

    if ("IntersectionObserver" in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            isVisible = true;
            if (!animationFrameId) {
              animationFrameId = requestAnimationFrame(loop);
            }
          } else {
            isVisible = false;
            if (animationFrameId) {
              cancelAnimationFrame(animationFrameId);
              animationFrameId = null;
            }
          }
        });
      }, { threshold: 0.05 });

      observer.observe(heroSection);
    } else {
      animationFrameId = requestAnimationFrame(loop);
    }
  }

  // B. Living Crossfade Slider
  function initHeroSlider() {
    const slides = document.querySelectorAll(".hero-slide");
    const dots = document.querySelectorAll(".hero-slide-dot");
    const container = document.querySelector(".hero-image-container");
    const heroFrame = document.querySelector(".hero-frame") || container;
    if (!slides.length) return;

    let currentIndex = 0;
    let slideTimer = null;
    const INTERVAL_MS = 6000;

    function goToSlide(index) {
      slides[currentIndex].classList.remove("active");
      if (dots[currentIndex]) dots[currentIndex].classList.remove("active");

      currentIndex = (index + slides.length) % slides.length;

      slides[currentIndex].classList.add("active");
      if (dots[currentIndex]) dots[currentIndex].classList.add("active");
    }

    function startTimer() {
      stopTimer();
      slideTimer = setInterval(() => {
        goToSlide(currentIndex + 1);
      }, INTERVAL_MS);
    }

    function stopTimer() {
      if (slideTimer) {
        clearInterval(slideTimer);
        slideTimer = null;
      }
    }

    dots.forEach((dot, idx) => {
      dot.addEventListener("click", () => {
        goToSlide(idx);
        startTimer();
      });
    });

    if (container) {
      container.addEventListener("mouseenter", stopTimer);
      container.addEventListener("mouseleave", startTimer);
    }

    // Touch / Swipe Support for Mobile & Tablet (matching Our Story timeline photo slider)
    if (heroFrame) {
      let touchStartX = 0;
      let touchStartY = 0;

      heroFrame.addEventListener(
        "touchstart",
        (e) => {
          stopTimer();
          if (e.changedTouches && e.changedTouches.length > 0) {
            const touch = e.changedTouches[0];
            touchStartX = touch.clientX !== undefined ? touch.clientX : touch.screenX;
            touchStartY = touch.clientY !== undefined ? touch.clientY : touch.screenY;
          }
        },
        { passive: true }
      );

      heroFrame.addEventListener(
        "touchend",
        (e) => {
          if (e.changedTouches && e.changedTouches.length > 0) {
            const touch = e.changedTouches[0];
            const touchEndX = touch.clientX !== undefined ? touch.clientX : touch.screenX;
            const touchEndY = touch.clientY !== undefined ? touch.clientY : touch.screenY;
            const diffX = touchStartX - touchEndX;
            const diffY = touchStartY - touchEndY;

            // Trigger if horizontal swipe is dominant and exceeds 35px threshold
            if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > 35) {
              if (diffX > 0) {
                goToSlide(currentIndex + 1);
              } else {
                goToSlide(currentIndex - 1);
              }
            }
          }
          startTimer();
        },
        { passive: true }
      );

      heroFrame.addEventListener(
        "touchcancel",
        () => {
          startTimer();
        },
        { passive: true }
      );
    }

    startTimer();
  }

  // C. Subtle 3D Depth Parallax on Desktop
  function initHeroParallax() {
    if (!window.matchMedia("(pointer: fine)").matches) return;

    const heroSection = document.getElementById("hero");
    const heroFrame = document.querySelector(".hero-frame");
    const heroSeal = document.querySelector(".hero-monogram-seal");
    if (!heroSection || !heroFrame) return;

    let targetRX = 0;
    let targetRY = 0;
    let currentRX = 0;
    let currentRY = 0;
    let isParallaxActive = false;

    heroSection.addEventListener("mousemove", (e) => {
      const rect = heroSection.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;

      targetRX = -y * 7;
      targetRY = x * 7;

      if (!isParallaxActive) {
        isParallaxActive = true;
        requestAnimationFrame(animateParallax);
      }
    });

    heroSection.addEventListener("mouseleave", () => {
      targetRX = 0;
      targetRY = 0;
    });

    function animateParallax() {
      currentRX += (targetRX - currentRX) * 0.08;
      currentRY += (targetRY - currentRY) * 0.08;

      heroFrame.style.transform = `perspective(1000px) rotateX(${currentRX.toFixed(2)}deg) rotateY(${currentRY.toFixed(2)}deg)`;
      if (heroSeal) {
        heroSeal.style.transform = `translate3d(${(-currentRY * 1.5).toFixed(1)}px, ${(currentRX * 1.5).toFixed(1)}px, 20px)`;
      }

      if (Math.abs(targetRX - currentRX) > 0.01 || Math.abs(targetRY - currentRY) > 0.01) {
        requestAnimationFrame(animateParallax);
      } else {
        isParallaxActive = false;
        heroFrame.style.transform = targetRX === 0 ? "none" : heroFrame.style.transform;
      }
    }
  }

  /* ==========================================================================
     8. OUR STORY RELATIONSHIP PHASE SLIDERS
     ========================================================================== */
  function initStorySliders() {
    const sliderFrames = document.querySelectorAll(".story-slider-frame");
    if (!sliderFrames.length) return;

    sliderFrames.forEach((frame) => {
      const track = frame.querySelector(".story-slider-track");
      const slides = frame.querySelectorAll(".story-slide");
      const prevBtn = frame.querySelector(".story-slider-btn.prev");
      const nextBtn = frame.querySelector(".story-slider-btn.next");
      const dots = frame.querySelectorAll(".story-slider-dot");
      const counter = frame.querySelector(".story-slider-counter");
      const captions = frame.querySelectorAll(".story-frame-captions .story-frame-caption");

      if (!track || !slides.length) return;

      let currentIndex = 0;
      const total = slides.length;

      function updateSlide(newIndex) {
        currentIndex = (newIndex + total) % total;

        // Slide the track
        track.style.transform = `translateX(-${currentIndex * 100}%)`;

        // Update counter
        if (counter) {
          counter.textContent = `${currentIndex + 1} / ${total}`;
        }

        // Update dots
        dots.forEach((dot, idx) => {
          dot.classList.toggle("active", idx === currentIndex);
        });

        // Update captions
        captions.forEach((caption, idx) => {
          caption.classList.toggle("active", idx === currentIndex);
        });
      }

      if (prevBtn) {
        prevBtn.addEventListener("click", (e) => {
          e.stopPropagation();
          updateSlide(currentIndex - 1);
        });
      }

      if (nextBtn) {
        nextBtn.addEventListener("click", (e) => {
          e.stopPropagation();
          updateSlide(currentIndex + 1);
        });
      }

      dots.forEach((dot, idx) => {
        dot.addEventListener("click", (e) => {
          e.stopPropagation();
          updateSlide(idx);
        });
      });

      // Touch / Swipe Support for Mobile & Tablet
      let touchStartX = 0;
      let touchStartY = 0;

      frame.addEventListener(
        "touchstart",
        (e) => {
          if (e.changedTouches && e.changedTouches.length > 0) {
            const touch = e.changedTouches[0];
            touchStartX = touch.clientX !== undefined ? touch.clientX : touch.screenX;
            touchStartY = touch.clientY !== undefined ? touch.clientY : touch.screenY;
          }
        },
        { passive: true }
      );

      frame.addEventListener(
        "touchend",
        (e) => {
          if (e.changedTouches && e.changedTouches.length > 0) {
            const touch = e.changedTouches[0];
            const touchEndX = touch.clientX !== undefined ? touch.clientX : touch.screenX;
            const touchEndY = touch.clientY !== undefined ? touch.clientY : touch.screenY;
            const diffX = touchStartX - touchEndX;
            const diffY = touchStartY - touchEndY;

            // Trigger if horizontal swipe is dominant and exceeds 35px threshold
            if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > 35) {
              if (diffX > 0) {
                updateSlide(currentIndex + 1);
              } else {
                updateSlide(currentIndex - 1);
              }
            }
          }
        },
        { passive: true }
      );
    });
  }

  // Initialize living hero & timeline features
  initHeroStardust();
  initHeroSlider();
  initHeroParallax();
  initStorySliders();
});

