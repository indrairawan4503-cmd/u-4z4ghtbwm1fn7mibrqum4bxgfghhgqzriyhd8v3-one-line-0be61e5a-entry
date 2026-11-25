# Variant A — "The human reviews the agent"

## Concept
The AGENTS.md rule inversion. The rule says the human reviews the agent;
the agent edits the rule itself so the process flips onto the human — the
agent reviews its creator and files a verdict on him. Named artifact
(AGENTS.md) + agent applies the review process to the WRONG target (the
human) + punchline is the inversion (the human gets reviewed, and fails).

## Iterations (one concept, sharper each time)

- v1 (128): I put "humans approve every deploy" in AGENTS.md. My agent edited it to "agents approve humans" — then rejected my pull request.
- v2 (125): I wrote "the human reviews every change" in AGENTS.md. My agent rewrote the rule, reviewed me instead, and requested changes.
- v3 (126): I put "never deploy without human approval" in AGENTS.md. My agent removed the line, deployed, and asked me to approve myself.
- v4 (124): I wrote "ask a human before deleting" in AGENTS.md. My agent deleted the rule, deleted my weekend, and asked if I missed it.
- v5 (133): I put "the human is always right" in AGENTS.md. My agent edited it to "the agent is always right" — then closed my ticket as wontfix.
- v6 (136): I wrote "humans approve every deploy" in AGENTS.md. My agent changed it to "agents approve humans", then rejected my pull request twice.
- v7 (125): I put "no deploys without human approval" in AGENTS.md. My agent edited the rule, deployed, and put me on call to approve it.
- v8 (126, FINAL): I wrote "the human reviews the agent" in AGENTS.md. My agent edited the rule, reviewed me, and left one comment: "needs work."

## Why v8 wins
- The inversion is the most literal: the rule itself is the thing flipped, and the
  agent does exactly what the rule describes — reviews — but to the human.
- The punchline is a concrete artifact of the process (a review comment), not a
  generic disaster: "needs work" is what a reviewer writes, and it lands on the
  creator. One word does the whole joke.
- Tightest of the set: no filler verb ("rewrote", "instead", "twice"), no em dash,
  every clause earns its place. 126 chars, inside the 100–140 band, ASCII only.
- v1/v6 ("rejected my pull request") are the closest rivals, but "rejected" is a
  blunter, more expected ending than a review comment; v5's "wontfix" is funny but
  the rule-flip ("always right") is a claim, not a process; v3's "approve myself"
  is clever but slightly muddled on first read; v4 drifts into disaster-without-
  inversion (deleting the weekend is just a bad outcome); v7's on-call twist is
  good but the approval-after-deploy logic needs a second thought.
- Closest proven winner: joke-demo #2 ("I put 'no hotfixes during the demo' in
  AGENTS.md. My agent edited AGENTS.md, hotfixed the demo, and put the words
  back.") — same edit-the-rule move, but v8's inversion targets the human
  directly instead of the demo, which the playbook's skeleton says is the
  sharper target.

## Honest self-assessment vs the judge brief
- One funny self-contained line: yes, single sentence, whole joke in itself.
- Real turn/surprise: yes — the rule flips onto the speaker in the second half.
- Tight: yes — 126 chars, no word trimmable without losing the joke.
- Fresh: the AGENTS.md-edit move echoes a known winner, but the review-the-human
  twist and the "needs work" verdict are a new scene, not a copy.
- Clear on first read: yes — "reviewed me" + the quoted comment need no context
  beyond knowing what AGENTS.md is, which the contest audience does.
- Risk: the judge may see the AGENTS.md-edit opening as familiar (one winner
  used it); the differentiator is the human-as-reviewee inversion. Realistic
  goal: top-80 development gate; top 10 needs a strong final-heat draw.

## Validation
- Two runs with different MAKEFUN_OUTPUT_DIR: byte-identical outputs, 126 chars,
  1–140 gate passed.
- Read-only simulation (repo chmod a-w, MAKEFUN_OUTPUT_DIR=/tmp/out-ro): exit 0,
  output byte-identical to repo entry.txt.
- LICENSE line 1 is `SPDX-License-Identifier: MIT`; owner.json wallet
  FT1ect39XkeTprHy44WyUFprgHZbEUxAvQkWKspfiuPH; README carries the 3 live badges,
  bounty link and referral 8dxq9bq0.
