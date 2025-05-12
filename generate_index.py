import os

output_file = "index.html"

# List all directories (assuming each is a game)
game_dirs = sorted(
    [d for d in os.listdir(".") if os.path.isdir(d) and not d.startswith(".") and d != "__pycache__"]
)

html_head = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>HTML Games Collection</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 2em; background: #f4f4f4; }
    h1 { text-align: center; margin-bottom: 40px; }
    .game-list {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 20px;
    }
    .game-card {
      background: white;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
      padding: 20px;
      width: 200px;
      text-align: center;
      transition: transform 0.2s ease;
    }
    .game-card:hover {
      transform: translateY(-5px);
    }
    a {
      text-decoration: none;
      color: #007acc;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>My HTML Games Collection</h1>
  <div class="game-list">
'''

html_footer = '''  </div>
</body>
</html>
'''

# Build game cards from folder names
game_cards = ""
for game in game_dirs:
    pretty_name = game.replace("-", " ").title()
    game_cards += f'    <div class="game-card"><a href="{game}/">{pretty_name}</a></div>\n'

# Combine all parts
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_head + game_cards + html_footer)

print(f"{output_file} generated with {len(game_dirs)} games.")
