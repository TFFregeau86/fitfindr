"""
The three FitFindr tools.

Each one is a standalone function you can call and test on its own, before any
of them are wired into the loop. Build and test them one at a time — three
untested tools joined by a loop is one problem that looks like six, because you
can't tell which layer is lying to you.

    search_listings(description, size, max_price)  → list[dict]
    suggest_outfit(new_item, wardrobe)             → str
    create_fit_card(outfit, new_item)              → str

All three are stubs right now. They run and they do nothing — that's the
starting position and it's deliberate.

⚠️ Before you write any of them, fill in the **Tool Inventory** section of your
README (Milestone 2). Four lines per tool: what it does, each input with its
type, exactly what it returns, and what it returns when it has nothing to give.
That last line is what your loop branches on. "Returns a list" earns nothing —
the description has to say what is *in* the list.
"""

import config  # noqa: F401 — you'll use this in search_listings
from generate import generate
from utils.data_loader import load_listings


# ── Tool 1: search_listings ───────────────────────────────────────────────────

def search_listings(
    description: str,
    size: str | None = None,
    max_price: float | None = None,
) -> list[dict]:
    """
    Search the listings data for items matching a description, size, and price.
    """
    listings = load_listings()

    # Turn the search description into lowercase keywords.
    keywords = description.lower().split()

    matches = []

    for listing in listings:
        # Price filter
        if max_price is not None and listing["price"] > max_price:
            continue

        # Size filter
        if size is not None:
            requested_size = size.strip().lower()
            listing_size = listing["size"].lower()

            # Split sizes such as "S/M" into individual size values.
            size_parts = [
                part.strip()
                for part in listing_size.replace("-", "/").split("/")
            ]

            if requested_size not in size_parts:
                continue

        # Score by keyword overlap with title, description, and style tags.
        searchable_text = " ".join(
            [
                listing["title"],
                listing["description"],
                *listing["style_tags"],
            ]
        ).lower()

        score = sum(1 for keyword in keywords if keyword in searchable_text)

        if score > 0:
            matches.append((score, listing))

    # Highest-scoring listings first.
    matches.sort(key=lambda item: item[0], reverse=True)

    return [
        listing
        for score, listing in matches[:config.SEARCH_RESULT_LIMIT]
    ]



# ── Tool 2: suggest_outfit ────────────────────────────────────────────────────

def suggest_outfit(new_item: dict, wardrobe: dict) -> str:
    """Suggest one or two outfits using the new item and wardrobe."""
    items = wardrobe.get("items", [])

    item_info = (
        f"Name: {new_item.get('title', '')}\n"
        f"Description: {new_item.get('description', '')}\n"
        f"Category: {new_item.get('category', '')}\n"
        f"Colors: {', '.join(new_item.get('colors', []))}\n"
        f"Style tags: {', '.join(new_item.get('style_tags', []))}"
    )

    if not items:
        prompt = f"""
Suggest one or two ways to style this secondhand clothing item.

{item_info}

The user has no wardrobe items entered yet, so give general styling advice.
Keep the suggestions practical and concise.
"""
    else:
        wardrobe_text = "\n".join(
            f"- {item.get('name', '')} | "
            f"category: {item.get('category', '')} | "
            f"colors: {', '.join(item.get('colors', []))} | "
            f"style: {', '.join(item.get('style_tags', []))}"
            for item in items
        )

        prompt = f"""
Suggest one or two outfits using this new secondhand item and pieces
the user already owns.

NEW ITEM:
{item_info}

USER'S WARDROBE:
{wardrobe_text}

Name the wardrobe pieces you use. Keep the suggestions practical and concise.
"""

    return generate(prompt)


# ── Tool 3: create_fit_card ───────────────────────────────────────────────────

def create_fit_card(outfit: str, new_item: dict) -> str:
    """
    Write a short caption someone would actually post about the find.

    Args:
        outfit: the outfit suggestion string from suggest_outfit().
        new_item: the listing dict for the item.

    Returns:
        A two-to-four sentence caption.
        If outfit is empty or whitespace, return a descriptive message.
    """
    if not outfit or not outfit.strip():
        return "I couldn't create a fit card because no outfit suggestion was provided."

    prompt = f"""
Write a short social-media-style fit card for this secondhand clothing find.

Item:
- Title: {new_item.get("title", "Unknown item")}
- Price: ${new_item.get("price", 0)}
- Platform: {new_item.get("platform", "unknown")}
- Brand: {new_item.get("brand") or "unbranded"}
- Colors: {", ".join(new_item.get("colors", []))}
- Style tags: {", ".join(new_item.get("style_tags", []))}

Outfit suggestion:
{outfit}

Write 2-4 sentences. Mention the item, its price, and platform once each.
Make it sound like a real post and describe the overall style/vibe.
Do not invent details that are not provided.
"""

    return generate(prompt).strip()
