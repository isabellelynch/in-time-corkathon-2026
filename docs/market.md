# Market

> Owner: Isabelle. Figures are sourced; anything not yet tested with real users is marked as a **hypothesis**.

## The customer

**Primary user: the owner or buyer at a small Irish importer.** A coffee roaster, a homewares shop, a bike dealer, a food wholesaler. They order by sea from outside the EU, often pay in dollars or sterling, and have no logistics team or treasury desk.

**Example: Niamh**, who runs a coffee roastery in Cork. 21 days of beans left; a new order from Santos via Rotterdam takes 35 days; invoiced in US dollars with the rate not fixed. She heard about a Rotterdam strike on the radio, a week after it started.

**Second user: their accountant.** Firms like FRAME advise many importing clients and are asked "should I order early?" and "why is my supplier charging more?" without a quick way to answer.

## Size

| Figure | Value | Source |
|---|---|---|
| Irish businesses importing goods, 2022 | **~49,600** | CSO, *Ireland's Trade in Goods 2022*, trade by enterprise size |
| Share that are small or medium | **98%** (36,365 micro, 9,768 small, 2,692 medium) | Same |
| Cafés in Ireland (coffee example only) | ~3,500 | Business listings (poidata.io), Dec 2025 / Jan 2026; not official |

Not every importer ships by sea from outside the EU or pays in a foreign currency; how many do is a **hypothesis to check** (the CSO publishes trade by partner country that could narrow it).

## The problem today

What a small importer does now, and why it fails:

| Today | Problem |
|---|---|
| News, radio, social media | Not matched to their ports; finds out late, or not at all |
| Phoning or emailing the freight forwarder | Only after they suspect a problem; forwarder is busy |
| Port and carrier websites | Scattered, technical, one site per port |
| The bank's FX quote | No easy way to tell whether the rate or margin is fair |
| Shipment-visibility platforms | Built and priced for large shippers, not a five-person business (**hypothesis**: to confirm in user interviews) |

The information is public; the work of joining it up isn't done for small firms.

## Alternatives: has this been done?

**For big companies, yes.** Supply-chain risk monitoring is an established category:

| Product | What it does | Built for |
|---|---|---|
| [Resilinc EventWatch](https://www.sdcexec.com/warehousing/news/11151547/resilinc-launches-eventwatch-professional-to-empower-businesses-to-monitor-and-detect-global-events-that-could-threaten-supply-chains) | 24/7 monitoring of 25+ event types (incl. port and labour strikes) from news sources, since 2013 | Procurement, sourcing and supply chain professionals |
| [GoComet Incident Lens](https://www.gocomet.com/products/incident-lens) | Tracks port strikes, weather and unrest; connects disruptions to a company's active freight; integrates with TMS/ERP | Logistics, operations, procurement and risk teams; sales-led pricing |
| Everstream, Interos, project44 and similar | Supply-chain risk and shipment visibility | Large shippers and enterprises |

**For small importers, we haven't found one.** (A quick search, not proof that none exists; to confirm in user interviews.)

| Big-company tools | In Time |
|---|---|
| For logistics and risk teams | For a five-person business, or their accountant |
| Need system integration (TMS/ERP) | Type your route; nothing to install, nothing stored |
| Sales-led pricing | Built on free public data (ECB, GDELT, CSO, Eurostat) |
| Delay risk | Delay **and** currency cost **and** your stock, in one answer |
| Dashboards of alerts | One plain-English answer, one next step |
| — | Says when it doesn't know; keeps rumour apart from confirmation |

**Positioning line:** *"Big companies have Resilinc and GoComet. Niamh has the radio. In Time gives small importers the same early warning, in plain English, with no setup."*

The existence of these tools is evidence the problem is real and worth paying for.

## What In Time does differently

- **Their route, their dates:** only news naming their ports.
- **Rumour vs fact:** "reported" news is kept apart from "confirmed" official notices.
- **Tied to their business:** stock against lead time; currency change on the part of the invoice not yet fixed; their bank's quote against the ECB rate.
- **Honest:** says when it can't tell, and what it couldn't check.
- **Private:** nothing typed is stored.
- **For accountants:** several clients on one page, re-checked every 30 minutes, with a plain summary to send.

## Who pays (hypotheses)

| Model | Why it might work | Risk |
|---|---|---|
| **Accountancy firms**, per adviser seat, offered to importing clients | Firms already advise on cash flow; a reason to talk to clients; FRAME is the sponsor | Firms need it to save time, not add a tool |
| Free for importers, paid alerts (email/text) | Low barrier; alerts are the clear upgrade | Conversion from free is usually low |
| Through banks or trade bodies (e.g. as a member benefit) | Reach to many SMEs at once | Slow partnerships |

Leading option for the pitch: **through accountants**, because it matches the sponsor and the "several shipments" feature already built.

## How we'd test it

1. **5 interviews** with small importers (Cork first): how did they hear about the last delay or price rise? What would they have done with two weeks' notice?
2. **3 interviews** with accountants at a firm like FRAME: how often do clients ask about stock or currency? Would they send an In Time summary?
3. **Pilot:** 10 importers' real routes checked weekly for a month; count how often In Time flagged something before they heard elsewhere.
4. **Measure:** days of warning gained; false alarms (target: none from "confirmed"); whether users act on the next step.

## Risks

| Risk | Mitigation |
|---|---|
| Users trust it too much | Every answer says what it can't see; never "no action needed" |
| Official notices can't be reused | Confirmation stays off until reuse terms are recorded; link to the notices instead |
| News misses quiet delays | Say so in every answer; encourage checking with the forwarder |
| Small firms won't enter details | A short form in three groups, folded into one line after the first answer; nothing stored |
