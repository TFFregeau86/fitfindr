FitFindr
Start here

New to this repo? Read RUNNING.md first — setup, every
command, and what to do when something breaks.

Once python test.py passes:

python app.py listings --full -n 6
python app.py fields
python app.py ask 'vintage graphic tee under $30'


All three tools are stubs, so the last command will not produce a useful
result yet. That is the starting position.

The rest of this file is your submission.

What This Does

FitFindr is an agent that helps a user find a secondhand clothing item based on a description, size, and maximum price. It searches the listings data and selects a matching item when one is available. The agent then uses the selected item and the user's wardrobe to suggest an outfit and creates a short fit-card caption. If no listings match the search, the agent stops and tells the user what they can change instead of trying to create an outfit without an item.

Tool Inventory
search_listings

What it does: Searches the listings data for items matching the requested description, size, and maximum price.

Inputs: description (string), size (string), max_price (float).

Returns: A list of listing dictionaries. Each listing contains id, title, description, category, style_tags, size, condition, price, colors, brand, and platform.

When it has nothing: Returns an empty list when no listings match the search criteria.

suggest_outfit

What it does: Uses the selected listing and the user's wardrobe to suggest ways to wear the new item.

Inputs: new_item (dictionary containing one listing), wardrobe (dictionary containing an items list of wardrobe-item dictionaries).

Returns: A string containing outfit suggestions that combine the new item with items from the user's wardrobe.

When it has nothing: When wardrobe["items"] is empty, returns general outfit advice for the new item instead of failing.

create_fit_card

What it does: Creates a short caption suitable for posting about the selected item and suggested outfit.

Inputs: outfit (string containing outfit suggestions), new_item (dictionary containing the selected listing).

Returns: A short string containing a social-media-style fit-card caption.

When it has nothing: Returns a valid short caption even if the outfit information is limited.

Planning Loop

Branch rule: If search_listings returns an empty list, the agent puts a message in the session and stops without calling suggest_outfit. Otherwise, it takes the first matching listing, stores it as session["selected_item"], and continues to suggest_outfit.

Where it lives: agent.py::run_agent

How the query is parsed: The query is parsed by the agent into the description, size, and maximum price values needed by search_listings. The exact parsing implementation will be documented here after the planning loop is built.

What moves through the session: The search results are stored in the session first. When results exist, the first listing is stored as session["selected_item"]. The outfit generated from that item is then stored in the session before being passed to create_fit_card. The final fit card is also stored in the session.

Sample Run

One full query

The planning loop has not been implemented yet, so the starter currently produces the following output:

$ python app.py ask 'vintage graphic tee under $30'

  The planning loop isn't built yet — see the TODO in agent.py.

0 model calls this session


The three tools, tested one at a time

These tests will be added after the three tools are implemented.

$ python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"

[Tool test output will be added after search_listings is implemented.]

$ python -c "from tools import suggest_outfit; ..."

[Tool test output will be added after suggest_outfit is implemented.]

$ python -c "from tools import create_fit_card; ..."

[Tool test output will be added after create_fit_card is implemented.]

How I Used AI

Moment 1

What I asked for: I asked AI to help me understand the fields in the listings data and use them to write specific tool specifications.

What came back: AI explained that search_listings should accept a description, size, and maximum price, and that it should return a list of listing dictionaries containing the fields from the listings data.

What I changed: I used that information to make my search_listings specification more specific and documented that it returns an empty list when there are no matches.

Moment 2

What I asked for: I asked AI to help me understand the wardrobe schema before writing the suggest_outfit specification.

What came back: AI pointed out that the wardrobe is a dictionary containing an items list, rather than being a plain list.

What I changed: I updated my suggest_outfit specification so that wardrobe is documented as a dictionary containing an items list of wardrobe-item dictionaries.

<!-- ═══════════════════════ UNIT 4 — THE TEST ═══════════════════════ -->
Run Log — Before
<!-- Leave this section for Unit 4. -->
Criterion	Target	Try 1	Try 2	Try 3	Try 4	Try 5	Verdict
1.							
2.							
3.							
4.							
5.							

Real output from one try, pasted as text, naming the file and function that produced it:



Verdicts and Diagnoses
#	Criterion	Target	Verdict	How I decided
1				
2				
3				
4				
5				

Diagnoses

Loop Trace

Happy path




Empty search




On the MCP move:

The Improvement

What I changed:

Which failure it was meant to fix:

Run Log — After
Criterion	Target	Try 1	Try 2	Try 3	Try 4	Try 5	Verdict
1.							
2.							
3.							
4.							
5.							

Did it help, and how do I know:

What's Still Broken

📖 How to run this project: RUNNING.md