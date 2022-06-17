from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2="0cfd36fd1408f4ddd9aaef5c8171130633c74a1927e904f8419eca3d1162532aa4c1f2b64a2fcf108cb3b42746896db44dd5f67fdb412dc0f21072634982587b3c22f489d6ffa6089d055ed95195")

# Replace this URL with the URL of the page you want to edit
page = client.get_block("https://www.notion.so/pedi406/Elasticsearch-43acc05b5085437e9ac26dcab1f1e351")
print(page.title)

print("The old title is:", page.title)

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
page.title = "The title has now changed, and has *live-updated* in the browser!"