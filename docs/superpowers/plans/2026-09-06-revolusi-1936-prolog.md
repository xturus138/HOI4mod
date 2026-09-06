# Default 1936 Revolution Prologue (84 Days) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the mod's opening experience into a canonical, story-driven 84-day prologue in early 1936 where the Indonesian Revolution erupts by default as the organic alternate-history progression, removing the artificial bypass decision.

**Architecture:** The shared national focus trunk is restructured into 3 sequential 28-day narrative focuses (total 84 days: January to late March 1936), keeping `dei_focus_momentum_kemerdekaan` at position `(12, 8)` to maintain perfect alignment for all 6 ideological branches. Events `dei_trunk.1` through `dei_trunk.5` are refactored into the 1936 economic and military crisis storyline, culminating in `dei_trunk.6`. The obsolete `dei_decision_revolusi_dini` is removed.

**Tech Stack:** Hearts of Iron IV (Clausewitz Engine scripting), YAML localisation (UTF-8 with BOM), Python verification scripts.

## Global Constraints
- Target Tag: `INS`
- Duration ceiling: Maximum 3 months (~84 days) from January 1, 1936.
- Preserved terminology: Authentic Indonesian historical/military/cultural terms must be preserved (Volksraad, KNIL, TKR, Proklamasi, Merdeka, Laskar, etc.).
- Localisation encoding: `DEI_indonesia_l_english.yml` MUST use UTF-8 with BOM (`\xef\xbb\xbf`).
- Coordinate integrity: 0 coordinate collisions across all national focus trees.
- Asset integrity: 100% valid event picture sprites (0 missing sprites).

---

### Task 1: Restructure Shared Trunk Focuses (`DEI_00_shared_trunk.txt`)

**Files:**
- Modify: `c:/Users/radit/Project/VisualStudioProject/Personal/HOI4MODS/Indonesia Sub Mod 56/HOI4mod/IndonesiaRayaR56/common/national_focus/DEI_00_shared_trunk.txt`

- [ ] **Step 1: Replace old 11-focus colonial tree with the 3-focus 1936 Revolutionary Prologue**
  Set up:
  - `dei_focus_root`: x = 12, y = 0, cost = 4 (28 days). Gives PP +40, stability -0.05, fires `dei_trunk.1`.
  - `dei_focus_pembangkangan`: x = 12, y = 4, cost = 4 (28 days), prerequisite = `dei_focus_root`. Gives war support +0.10, stability -0.05, fires `dei_trunk.2`.
  - `dei_focus_momentum_kemerdekaan`: x = 12, y = 8, cost = 4 (28 days), prerequisite = `dei_focus_pembangkangan`. Fires `dei_trunk.6` (Momentum Kemerdekaan Telah Tiba).
- [ ] **Step 2: Verify brace matching and focus IDs**
  Ensure braces balance and no invalid syntax exists.

---

### Task 2: Refactor Trunk Narrative Events (`DEI_00_shared_trunk_events.txt`)

**Files:**
- Modify: `c:/Users/radit/Project/VisualStudioProject/Personal/HOI4MODS/Indonesia Sub Mod 56/HOI4mod/IndonesiaRayaR56/events/DEI_00_shared_trunk_events.txt`

- [ ] **Step 1: Update storyline events for 1936 crisis**
  - `dei_trunk.1`: Retaknya Pax Neerlandica: Gelombang Pemogokan Umum & Krisis Kepercayaan 1936.
  - `dei_trunk.2`: Pembangkangan di Barak Militer KNIL & Sabotase Jalur Kereta Api.
  - `dei_trunk.3`: Respon Keras Batavia: Represi vs Dialog yang Gagal.
  - `dei_trunk.4`: Konsolidasi Barisan Pemuda & Komite Perjuangan Bawah Tanah.
  - `dei_trunk.5`: Hilangnya Kendali Kolonial di Pulau Jawa.
  - `dei_trunk.6`: Proklamasi Revolusi Nasional 1936 (remains the pivotal ideological gateway to 6 paths with starter army, navy, air wing, and commanders).
- [ ] **Step 2: Verify event pictures and triggers**
  Ensure all events keep valid pictures (`GFX_report_event_...`).

---

### Task 3: Remove Artificial Shortcut Decision

**Files:**
- Modify: `c:/Users/radit/Project/VisualStudioProject/Personal/HOI4MODS/Indonesia Sub Mod 56/HOI4mod/IndonesiaRayaR56/common/decisions/DEI_decisions.txt`
- Remove: `c:/Users/radit/Project/VisualStudioProject/Personal/HOI4MODS/Indonesia Sub Mod 56/HOI4mod/IndonesiaRayaR56/events/DEI_01_revolusi_dini_events.txt`

- [ ] **Step 1: Remove `dei_decision_revolusi_dini` from decisions**
  Remove the bypass decision and clean up any obsolete references.
- [ ] **Step 2: Clean up obsolete decision event file**
  Delete or retire `events/DEI_01_revolusi_dini_events.txt`.

---

### Task 4: Update English Localisation with Authentic Terms

**Files:**
- Modify: `c:/Users/radit/Project/VisualStudioProject/Personal/HOI4MODS/Indonesia Sub Mod 56/HOI4mod/IndonesiaRayaR56/localisation/english/DEI_indonesia_l_english.yml`

- [ ] **Step 1: Add/update localization keys for the 3 prologue focuses and updated narrative events**
  Include title, descriptions, and option texts for all new/updated prologue focuses and events.
- [ ] **Step 2: Ensure UTF-8 with BOM encoding is strictly preserved**
  Verify `\xef\xbb\xbf` header.

---

### Task 5: Verification & Audit Scripts

**Files:**
- Modify: `C:/Users/radit/.gemini/antigravity-ide/brain/cab89a6c-9f62-41de-abd4-a13bc7cc8cc0/scratch/final_verification.py`
- Modify: `c:/Users/radit/Project/VisualStudioProject/Personal/HOI4MODS/Indonesia Sub Mod 56/HOI4mod/AGENTS.md`
- Modify: `c:/Users/radit/Project/VisualStudioProject/Personal/HOI4MODS/Indonesia Sub Mod 56/HOI4mod/IndonesiaRayaR56/README.md`

- [ ] **Step 1: Run comprehensive verification script**
  Run `final_verification.py` (check braces, event pictures, 0 focus collisions).
- [ ] **Step 2: Run localization audit**
  Run `verify_all_loc.py` (0 missing keys).
- [ ] **Step 3: Run asset audit**
  Run `comprehensive_asset_audit.py` (0 missing sprites/flags).
- [ ] **Step 4: Update documentation**
  Update AGENTS.md and README.md with the canonical 1936 Revolutionary Prologue architecture.
