# Renderer Notes

Preview cards are currently typography-first.

They intentionally do not render:

- avatar artwork
- avatar/background panels
- block-logo overlays inside artwork panels

If avatars are reintroduced later, keep the renderer change small:

- add the artwork block inside `render_preview_card` after the meta/open row
- keep artwork loading out of shared helpers unless multiple renderers use it
- add CSS only for the active artwork block, not dormant legacy selectors
- test a few cards visually before reconnecting all artwork
