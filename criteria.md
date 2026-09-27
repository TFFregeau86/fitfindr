# Acceptance criteria — FitFindr

Five criteria that say what "working" means for this agent, written in unit 3
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"The agent handles errors"* is an opinion.
*"When search returns nothing, the agent stops before calling the second tool,
in 5 of 5 tries"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter one. A reason that says something about your tools, your loop, or the
data earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

**Two are written for you. You write three.**

---

## 1. A matching query completes all three tools

Given a query that matches at least one listing, the agent completes all three
tool calls and returns a fit card — in at least 4 of 5 tries.

**Why this target:**
I chose 4 of 5 because the search uses matching rules that may not recognize
every possible way a user could phrase a request. Allowing one miss gives the
agent some room for variation while still requiring it to complete the happy
path reliably.

---

## 2. An impossible query stops before the second tool

Given a query that matches no listings, the agent stops before calling
`suggest_outfit` and returns a message naming what to change — 5 of 5 tries.

**Why this target:**
I chose 5 of 5 because an empty search is a clear condition that the program
can check directly. Once the search returns an empty list, the loop should
always take the same stop branch instead of depending on model-generated
wording.

3. When search_listings returns a matching listing, the exact listing stored
   as session["selected_item"] is passed to suggest_outfit in 5 of 5 runs.

Reason:
The selected listing is the information that connects the search step to the
outfit step, so I want to verify that the same item is carried through the
session every time.

4. When create_fit_card receives a valid item and outfit, it returns a
   non-empty caption that refers to the new item in at least 4 of 5 runs.

Reason:
The model may use different wording on different runs, so I am checking
that the captions remain relevant instead of requiring identical wording.

5. For 5 test queries with known matching listings, every listing returned by
   search_listings has a price at or below max_price and a size matching the
   requested size.

Reason:
Price and size are explicit search inputs, so the returned listings should
respect both constraints.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 4 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 4. Something about the fit card

         The fit card is different every time.

         **Why this target:** ...

         > **Revised in unit 4:** For 5 different items, the 5 fit cards share
         > no opening sentence.
         >
         > **Why revised:** "different" wasn't checkable — two cards that
         > differed by one word still counted. The new version is something I
         > can actually score.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said the empty search stops it 5 of 5 times, but I got 3 of 5,
            so 3 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
