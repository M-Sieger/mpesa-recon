# MVP Plan – M-Recon (Validation + Build + Pilot)

**Created:** 21. Oktober 2024  
**Updated:** 13. Januar 2025  
**Version:** 2.0 (Strategic Pivot)  
**Timeline:** Phase 0-2 (Jan 13 - Jun 30, 2025)

---

## Overview

**Mission:** Validate loan-access value proposition with SACCOs, build MVP, launch 3 SACCO pilots with 1,500 users.

**Three Phases:**
1. **Phase 0: Validation** (Jan 13-27) - Prove SACCO interest + PDF parsing + WTP
2. **Phase 1: MVP Build** (Feb 1 - Mar 31) - Build product (8 weeks)
3. **Phase 2: Pilot Launch** (Apr 1 - Jun 30) - 3 SACCO pilots, 1,500 users

**Total Budget:** ~USD $15K (KES 2M)
- Phase 0: $500 (Grace interviews, PDFs, LinkedIn premium)
- Phase 1: $10K (Freelancer devs, Supabase, hosting)
- Phase 2: $4.5K (Marketing, support, partnership travel)

---

## PHASE 0: VALIDATION (Jan 13-27, 2025) ← CURRENT

### Goal
**Validate 4 Critical Assumptions Before Committing to MVP Build**

### Success Criteria (GO/NO-GO Decision Gate)
```yaml
STRONG GO:
  ✅ 2+ SACCO conversations with strong interest (verbal LOI)
  ✅ PDF parsing PoC: 85-90%+ accuracy on 20 real PDFs
  ✅ 30+ waitlist signups
  ✅ 60%+ WTP at KES 500/mo (10 Grace interviews)
  
YELLOW (Adjust & Retry):
  ⚠️ 1 SACCO conversation, weak interest
  ⚠️ 70-80% parsing accuracy
  ⚠️ 10-20 signups
  ⚠️ 40-50% WTP
  
RED STOP:
  ❌ 0 SACCO interest after 10+ outreach attempts
  ❌ <70% parsing accuracy
  ❌ <10 signups
  ❌ <30% WTP
```

### Week 1 (Jan 13-19, 2025)

#### Monday (TODAY)
- [x] Update documentation (README, PRODUCT-VISION)
- [ ] **SACCO Outreach:** LinkedIn messages to 5 CEOs
  - Kimisitu SACCO (Enterprise IT winner)
  - Finmat SACCO (AI/data focus)
  - Tower SACCO (Member empowerment)
  - Police SACCO (M-Tawi success)
  - Kenya Re SACCO (Bank statement requirements)
- [ ] **PDF Sourcing:** Download 3 M-Pesa PDFs from Scribd/sources
  - Esther (1-page sample)
  - Kenneth (3-page sample)
  - David (8-page 2025 sample)

#### Tuesday-Wednesday
- [ ] **PDF Parsing PoC:**
  - Test PDFPlumber on 3 downloaded PDFs
  - Measure accuracy: Transactions extracted vs manual count
  - Document edge cases (date formats, special characters)
  - Target: 85%+ accuracy
- [ ] **Waitlist Page Update:**
  - Change messaging from "bookkeeping" to "loan-access"
  - Headline: "Turn Your M-Pesa History Into Loan Approval"
  - Add: "Trusted by [X] SACCOs" (placeholder)
  - Deploy via Vercel
- [ ] **Grace Coordination:**
  - Schedule 10 SME interviews (Thu-Fri this week + next week)
  - Brief Grace on questions:
    1. Have you applied for a SACCO/bank loan? (Y/N)
    2. Were you rejected? Why? (If rejected)
    3. Would you pay KES 500/mo for loan-ready financial reports?
    4. Are you a SACCO member? Which one?

#### Thursday-Friday
- [ ] **Grace Interviews:** Execute 5-10 interviews
  - Record WTP responses (Yes/No/Maybe)
  - Capture verbatims about loan rejection experiences
  - Identify SACCO memberships (for partnership targeting)
- [ ] **WEF Email:** Send partnership inquiry to Rachel Musyoki
  - Subject: "Partnership Opportunity: Help WEF Members Access Bank Accounts"
  - Pitch: M-Recon helps meet bank account documentation requirements
  - Low priority (WEF is long-term play)
- [ ] **SACCO Follow-ups:** Respond to LinkedIn replies
  - If interest: Schedule Zoom call for Week 2
  - Prepare demo deck (simple slides, no product yet)

### Week 2 (Jan 20-27, 2025)

#### Monday-Tuesday
- [ ] **PDF Parsing Expansion:**
  - Source 17 more PDFs (Total: 20 PDFs)
  - Grace network, Upwork redaction service, Scribd
  - Test PDFPlumber on all 20
  - Calculate final accuracy: Extract transactions vs manual validation
  - Document: Which PDF formats work best? Edge cases?
- [ ] **SACCO Calls:** 2-3 Zoom meetings
  - Present pitch deck:
    - Problem: 29% loan rejections due to missing docs
    - Solution: M-Recon turns M-Pesa PDFs into loan-ready reports
    - Ask: "Would you pilot this with 100 members for free?"
  - Record interest level: Hot/Warm/Cold
  - If Hot: Draft simple LOI (Letter of Intent)

#### Wednesday-Thursday
- [ ] **Metrics Check:**
  - Waitlist signups: Count total
  - Grace interviews: Calculate % WTP Yes
  - PDF parsing: Final accuracy %
  - SACCO interest: # of Hot leads
- [ ] **Decision Prep:**
  - Compile validation results into 1-page summary
  - Budget planning if GO (Phase 1 costs)
  - Identify gaps if YELLOW (what to improve?)

#### Friday (Jan 27) - DECISION GATE
- [ ] **GO/PIVOT/STOP Decision:**
  - Review all 4 metrics (SACCO, parsing, signups, WTP)
  - If GO: Start Phase 1 planning (hire freelancers, tech setup)
  - If YELLOW: Define pivot strategy, retry for 2 more weeks
  - If STOP: Document learnings, consider alternative markets

### Budget: Phase 0
- LinkedIn Premium (SACCO outreach): $30
- Grace interviews (10 × KES 500 = $40): $40
- PDF sourcing (Upwork redaction, if needed): $100
- Waitlist page updates (freelance design, optional): $200
- Miscellaneous (phone credit, coffee for interviews): $130
- **Total: ~$500**

---

## PHASE 1: MVP BUILD (Feb 1 - Mar 31, 2025)

### Goal
**Ship working product: Backend API + Web App + Android MVP**

### Team
- **You (Founder):** Product manager, backend development, SACCO partnerships
- **Freelancer 1 (Full-Stack Web):** React frontend, Vercel deployment (20 hours/week, 8 weeks)
- **Freelancer 2 (React Native):** Android app, offline-first architecture (20 hours/week, 8 weeks)
- **Grace (Part-Time):** User testing, Nairobi-based support (10 hours/week, 8 weeks)

### Timeline: 8 Weeks

#### Week 1-2 (Backend Foundation)
**Your Work:**

- [ ] **FastAPI Backend Setup:**
  - Supabase account setup (free tier)
  - FastAPI project structure
  - Supabase Auth integration (email/phone OTP)
  - PostgreSQL schema design (users, uploads, transactions)
- [ ] **PDF Parsing Pipeline:**
  - PDFPlumber integration
  - Password decryption (ID number input)
  - Transaction extraction logic (from Phase 0 learnings)
  - Edge case handling (date formats, special characters)
  - Target: 90%+ accuracy on test suite (20 PDFs from validation)
- [ ] **API Endpoints:**
  - POST /upload (PDF file)
  - GET /transactions (list for user)
  - POST /categorize (bulk categorization)
  - GET /report (generate financial summary)

**Freelancer 1 (Web):**
- [ ] **React Waitlist/Onboarding:**
  - Update existing client/ codebase
  - Waitlist → Signup flow
  - Email verification
  - Basic dashboard (upload button, transaction list placeholder)
- [ ] **Vercel Deployment:**
  - Environment variables (Supabase keys)
  - Deploy production + staging

#### Week 3-4 (Mobile MVP)
**Freelancer 2 (React Native):**
- [ ] **React Native + Expo Setup:**
  - Expo project init
  - Navigation (React Navigation)
  - Supabase Auth integration
  - Offline-first architecture (expo-sqlite)
- [ ] **Core Screens:**
  - Login/Signup (OTP via Supabase)
  - Upload PDF (expo-document-picker)
  - Enter ID number (for password)
  - Transaction List (offline-first, sync when online)
  - Categorization UI (bulk edit, smart suggestions)
  - Report Preview (PDF/CSV generation)
- [ ] **Offline Sync:**
  - SQLite schema mirroring PostgreSQL
  - Background sync (Expo Task Manager)
  - Conflict resolution (last-write-wins)

#### Week 5-6 (Integrations + Polish)
**Your Work:**
- [ ] **Financial Report Generation:**
  - PDF template (M-Recon Certified Financial Summary)
  - 6/12 month summaries (Total Income, Expenses, Profit)
  - WhatsApp share functionality
  - CSV export for eTIMS manual entry
- [ ] **SACCO Pilot Deck:**
  - 10-slide pitch deck (Problem, Solution, Pilot Terms)
  - Demo video (3 min: Upload → Categorize → Export)
  - LOI template (free for first 100 members)

**Freelancer 1+2:**
- [ ] **Polish & Bug Fixes:**
  - UI improvements (Material Design 3 for mobile)
  - Loading states, error handling
  - Accessibility (TalkBack support)
- [ ] **Testing:**
  - Unit tests (backend parsing, categorization logic)
  - Integration tests (API endpoints)
  - E2E tests (critical user flows: upload → report)

#### Week 7-8 (Beta Testing + SACCO Prep)
- [ ] **Internal Beta:**
  - TestFlight/Google Play Internal Track deployment
  - 5-10 internal testers (Grace + network)
  - Bug bash week
- [ ] **SACCO Outreach Round 2:**
  - Re-engage 2-3 SACCOs from Phase 0
  - Demo walkthrough (working product!)
  - Negotiate pilot terms:
    - Free for first 100 members
    - 3-month pilot (Apr-Jun)
    - Success metrics: 50% adoption, 15% loan approval uplift
- [ ] **Pilot Prep:**
  - Co-branded reports (SACCO logo)
  - Onboarding materials (Swahili + English)
  - Support playbook (WhatsApp FAQ)

### Deliverables (End of Phase 1)
✅ **Backend API:** FastAPI + Supabase (deployed on Railway/Fly.io)  
✅ **Web App:** React waitlist/dashboard (deployed on Vercel)  
✅ **Android MVP:** React Native app (TestFlight/Google Play Beta)  
✅ **PDF Parsing:** 90%+ accuracy on production  
✅ **SACCO Pilot Deck:** Ready to present  
✅ **2-3 SACCO LOIs:** Signed commitments for pilot

### Budget: Phase 1
- Freelancer 1 (Web): $50/hr × 20 hrs/week × 8 weeks = $8,000
- Freelancer 2 (Mobile): $50/hr × 20 hrs/week × 8 weeks = $8,000
- Supabase (Pro tier): $25/mo × 2 months = $50
- Railway/Fly.io (Backend hosting): $20/mo × 2 months = $40
- Vercel (Pro, if needed): $20/mo × 2 months = $40
- Domain name (m-recon.com): $20
- Grace (User testing): KES 10K/month × 2 = $150
- Miscellaneous (design assets, tools): $700
- **Total: ~$10,000**

**Budget Optimization (If Tight):**
- DIY mobile dev (React Native easier than Kotlin): Save $8K
- Use Supabase free tier: Save $50
- No separate web freelancer (focus mobile only): Save $8K
- **Minimum viable: ~$2,000** (just backend costs + Grace)

---

## PHASE 2: PILOT LAUNCH (Apr 1 - Jun 30, 2025)

### Goal
**Launch 3 SACCO pilots, achieve 1,500 users, measure loan approval uplift**

### Pilot Partners (From Phase 0-1)
**Partner A:** 10K members, target 500 users (5% adoption)  
**Partner B:** 8K members, target 400 users (5% adoption)  
**Partner C:** 15K members, target 600 users (4% adoption)  
**Total Target:** 1,500 users

### Timeline: 3 Months

#### Month 1 (Apr 1-30): Onboarding Wave 1
- [ ] **SACCO Partnership Kickoff:**
  - Joint announcement (SACCO newsletter, WhatsApp groups)
  - Co-branded materials (M-Recon + SACCO logo)
  - Training for SACCO loan officers (how to read M-Recon reports)
- [ ] **User Onboarding:**
  - Week 1: 50 users per SACCO (150 total)
  - Week 2: 100 users per SACCO (300 total)
  - Week 3: 150 users per SACCO (450 total)
  - Week 4: 200 users per SACCO (600 total)
- [ ] **Support:**
  - WhatsApp support group (Grace + you)
  - Daily monitoring (crash reports, parsing errors)
  - Weekly check-ins with SACCO liaisons

#### Month 2 (May 1-31): Scale + Measure
- [ ] **Continued Onboarding:**
  - Week 5-8: 50-75 new users/week per SACCO
  - Target by end of May: 1,200 total users
- [ ] **Loan Tracking:**
  - Identify users who submit loan applications
  - Track approval/rejection (via SACCO partner data)
  - Compare vs control group (members who didn't use M-Recon)
- [ ] **Product Iteration:**
  - Weekly product updates based on feedback
  - Bug fixes (aim for <1% crash rate)
  - Feature requests logged for Phase 3

#### Month 3 (Jun 1-30): Optimization + Results
- [ ] **Final Onboarding Push:**
  - Target: 1,500 users by Jun 30
  - Email/WhatsApp campaigns to inactive SACCO members
- [ ] **Success Metrics Measurement:**
  - Adoption Rate: % of SACCO members who signed up
  - Parsing Accuracy: User-reported (survey)
  - Loan Approval Uplift: M-Recon users vs control
  - Churn Rate: % of users who stopped using after 1 month
  - NPS: Net Promoter Score survey
- [ ] **Pilot Results Report:**
  - 10-page report for each SACCO
  - Present to SACCO board (decision on Phase 3 partnership)
  - If successful: Negotiate ongoing terms (KES 10K-25K/mo)
- [ ] **Seed Fundraising Prep:**
  - Update pitch deck with pilot results
  - Approach FSD Kenya (grant application)
  - Reach out to Acumen/Novastar (warm intros)

### Success Criteria (Pilot)
✅ **50%+ adoption** within pilot SACCO groups (750/1500 target)  
✅ **90%+ parsing accuracy** (user-reported surveys)  
✅ **15-20% loan approval uplift** (measured vs control group)  
✅ **<10% monthly churn** (users still active after 1 month)  
✅ **NPS 4+** (on 1-5 scale)

### Budget: Phase 2
- Grace (Full-time support): KES 50K/month × 3 = $1,150
- Marketing (SACCO co-marketing): $500
- Server costs (Supabase Pro + Railway): $150
- Partnership travel (Nairobi meetings): $200
- User incentives (first 100 users per SACCO): $500
- Miscellaneous (swag, materials): $200
- **Total: ~$2,700**

### Funding Target (If Pilot Successful)
**Seed Round: USD $250K-500K**
- FSD Kenya Grant: $50-100K
- Acumen/Novastar Seed: $250-400K

**Use of Funds:**
- Team expansion (2 devs, 1 sales, 1 support): $200K
- Scale to 10 SACCOs: $100K (marketing, partnerships)
- eTIMS integration development: $50K
- Operations + runway (6 months): $150K

---

## Post-Phase 2: Next Steps

### If Pilot Succeeds (all 5 success criteria met):
→ **Phase 3: SCALE (Jul-Dec 2025)**
- Target: 10 SACCOs, 10,000 users
- Revenue: KES 5M ARR (break-even)
- New features: eTIMS API, ML categorization, USSD
- See [`ROADMAP.md`](./ROADMAP.md) for details

### If Partial Success (3-4 criteria met):
→ **Pivot Sprint (30 days)**
- Identify weak points (adoption? parsing? churn?)
- Adjust pricing, features, or GTM
- Retry pilot with learnings

### If Failure (<3 criteria met):
→ **Critical Review**
- Product-market fit not achieved
- Options: Pivot to different market (banks, Tanzania), or stop

---

## Key Metrics Dashboard (Track Weekly)

### Acquisition
- New signups (total, per SACCO)
- Signup source (SACCO referral, organic, ads)

### Activation
- % users who upload PDF (activation rate)
- Time to first upload (TTFV)
- Parsing success rate

### Engagement
- MAU (Monthly Active Users)
- Avg reports generated per user
- WhatsApp shares (proxy for loan applications)

### Retention
- Day 7, 14, 30 retention
- Monthly churn rate

### Revenue (Post-Pilot)
- Free → Paid conversion
- MRR (Monthly Recurring Revenue)
- ARPU (Average Revenue Per User)

### Impact (Loan Access)
- # of reports shared with SACCOs
- Loan approval rate (M-Recon users vs control)
- Loan amounts approved

---

## Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| SACCOs don't deliver users | Medium | High | Over-recruit (5 SACCOs, need 3) |
| PDF format changes | Low | High | Flexible parser, community reporting |
| Users don't pay post-pilot | Medium | Medium | Strong loan-access value prop, free tier |
| Parsing accuracy <90% | Low | High | Hybrid (auto + manual review UI) |
| Competition (Pay Hero pivots) | Low | Medium | Speed + SACCO lock-in |

---

## Team & Tools

### Team (Phase 1)
- **You:** Product, backend, SACCO partnerships
- **Freelancer 1:** Frontend (React)
- **Freelancer 2:** Mobile (React Native)
- **Grace:** User testing, support (part-time)

### Team (Phase 2)
- **You:** CEO, partnerships, product
- **Grace:** Full-time support, user onboarding
- **(Future hire):** Mobile dev (after funding)

### Tools
- **Code:** GitHub
- **Project:** Notion or GitHub Projects
- **Design:** Figma
- **Communication:** Slack, WhatsApp
- **Analytics:** Mixpanel (user tracking)
- **Support:** WhatsApp Business
- **CI/CD:** GitHub Actions

---

## Summary: 6-Month Timeline

| Phase | Duration | Goal | Budget | Key Milestone |
|-------|----------|------|--------|---------------|
| **Phase 0** | Jan 13-27 | Validation | $500 | GO/NO-GO Decision |
| **Phase 1** | Feb 1 - Mar 31 | MVP Build | $10K | Working Product + SACCO LOIs |
| **Phase 2** | Apr 1 - Jun 30 | Pilot Launch | $2.7K | 1,500 users, prove uplift |
| **Total** | **6 months** | **PMF Validation** | **$13.2K** | **Seed Funding ($250-500K)** |

---

## Next Document

See [`ROADMAP.md`](./ROADMAP.md) for Phase 3 (Scale: Jul-Dec 2025) and beyond.

---

**Version History:**
- v1.0 (21.10.2024) – Initial 90-day plan (bookkeeping focus)
- v2.0 (13.01.2025) – Strategic pivot (loan-access + SACCO partnerships, 6-month plan)

---

**END OF MVP PLAN v2.0**
