# 30-Minute Client Technical Discovery Playbook

Great Forward Deployed Engineers don't start writing code until they understand the **exact operational bottleneck, data reality, and security boundary**. Here is a battle-tested 30-minute agenda for your first call with an enterprise client.

---

## Minutes 0–5: Problem & Success Metric Alignment
*Avoid jumping straight into tech stack choices.* Ask:
1. **"What manual workflow is costing your team the most hours or revenue right now?"**
2. **"If we demo a working prototype in 72 hours, what exact outcome makes your leadership say 'ship this'?"**
3. **"Who is the actual daily end-user, and how do they consume results today (Slack, Excel, internal web portal, ERP)?"**

---

## Minutes 5–15: Data Sources & Integration Reality
Enterprise pilots stall when data turns out to be trapped behind manual approvals or missing schemas. Probe specifically:
1. **"Where does the source data live today?"** *(SQL database, REST API, SFTP CSV drops, SharePoint PDFs, Snowflake?)*
2. **"How often does it update, and what is the approximate volume?"** *(10k rows/day vs. 50M historical records)*
3. **"Can we get a sanitized/redacted sample export of 100 rows or 20 PDFs today so we don't block on VPC firewall tickets?"** *(Crucial FDE hack to maintain 48-hour momentum!)*

---

## Minutes 15–23: Security, Identity & Deployment Constraints
Uncover blockers early so IT/InfoSec doesn't kill the pilot in Week 3:
1. **"Does your security team require deployment inside your own cloud VPC / on-prem cluster, or is an isolated single-tenant cloud environment acceptable for the pilot?"**
2. **"Which identity provider do employees use (Okta, Microsoft Entra ID, Google SSO)?"**
3. **"Are there PII, HIPAA, SOC2, or GDPR residency constraints on where logs or LLM inference can run?"**

---

## Minutes 23–30: Scope Lock & 48-Hour Prototype Plan
End the call with crystal-clear ownership:
- Summarize **3 concrete deliverables** for the Friday demo (explicitly list what is *out of scope* for v1).
- Confirm exact owners for:
  1. Sample dataset / API sandbox credentials
  2. Technical point of contact on Slack/Teams
  3. Friday 20-minute live demo calendar invite
