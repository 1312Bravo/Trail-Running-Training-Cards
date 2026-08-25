# Card Art Prompt Guide

This is the working prompt contract for training-card artwork. It records the visual direction agreed during exploration and should be refined through a small pilot before it becomes a final production guide.

## Purpose

Create original guardian artwork that gives training cards a collectible-card feeling without copying existing games, characters, card layouts, or artwork. The visual must support the coaching card, not replace its content.

## Master Visual

Every image in a visual family should preserve these foundations:

- Minimal graphic guardian art with a strong clean silhouette, a deep-slate fill, one or two broad inner shade planes, and a small number of precise contour lines. It should feel mature, mystical, and collectible: neither photorealistic nor a loose sketch, cartoon, painting, or stone sculpture.
- A dark navy and blue-gray alpine atmosphere with soft mist.
- A guardian avatar in deep slate tones with no fur, feather, scale, or material texture beyond the minimum lines needed to define its form.
- One planning-level neon contour light and a restrained mystical glow.
- A quiet dark-navy background with thin mountain-line art, one large halo arc, and a subtle winding trail line.
- One small muted-gold lineage mark, normally placed on the shoulder.
- Portrait-oriented framing with the avatar as the clear focal point.

The preferred Macro reference is a mature alpine ibex guardian: clean close three-quarter silhouette, large simply segmented horns, calm direct gaze, glacier-blue contour light, mountain-line background, halo arc, winding trail, and muted-gold shoulder mark.

## Reference Lock

The first four ibex renders are the canonical visual-world reference. Future avatar experiments must match their world before introducing a new species or degree of stylisation.

Keep these elements effectively unchanged:

- Dark, uncluttered navy-blue backdrop, with little or no atmospheric texture; never a detailed natural landscape or realistic mountain valley.
- A large, thin, pale halo arc behind the avatar.
- Sparse pale mountain *line art*, not rendered mountain terrain.
- One quiet winding route line in the lower background.
- Close portrait or compact full-body composition with the guardian filling most of the frame.
- One planning-level contour light, cool slate body palette, and one restrained muted-gold lineage mark.

When testing a new avatar, change only its species and its controlled degree of stylisation. Do not reinterpret the background, framing, lighting system, or overall palette. Use an approved reference image whenever generation supports it.

## Planning-Level Progression

For a chosen visual lineage, the planning levels are a generational progression. They must share recognizable anatomy, markings, materials, and world, but differ immediately through age, pose, and neon accent color.

| Planning level | Visual role | Pose and age | Accent color |
| --- | --- | --- | --- |
| Macro | Master guardian | Mature, imposing, calm, mostly still; largest horns and broadest frame | Glacier blue |
| Mezzo | Adult child | Slightly slimmer, smaller horns, deliberate forward walk | Neon emerald |
| Micro | Younger descendant | Compact, agile, alert side-step or light hop | Electric violet |
| Session | Youngest descendant | Lean, focused, short streamlined horns, precise forward stride | Neon amber |

The neon color should be limited to rim light and a faint trail glow. It should not recolor the whole avatar or overpower the shared slate-blue world.

## Relationship Rule

The literal parent-to-child treatment is a visual-storytelling option for one curated four-card lineage. It is not an automatic consequence of coaching relationships:

- Coaching links form a graph, so a card can be relevant below multiple valid parents.
- Each card still needs one stable approved artwork.
- When a card belongs to more than one pathway, use shared markings, a related lineage mark, and UI context rather than generating conflicting child versions.
- A future art catalog will explicitly choose the primary visual lineage for a card before artwork is generated.

Different Macro cards may use different mature guardian species. Their selected Mezzo, Micro, and Session descendants should inherit clear family traits such as face shape, horn or ear structure, markings, and the gold lineage mark.

## Prompt Template

Use the master section unchanged for every render in one visual family. Add only one planning-level variation section at a time.

```text
Use case: stylized-concept
Asset type: original training-card guardian artwork

Master visual:
Create minimal graphic guardian art with a strong clean silhouette, a deep-slate fill, one or two broad inner shade planes, and a small number of precise contour lines. It should feel mature, mystical, and collectible: neither photorealistic nor a loose sketch, cartoon, painting, or stone sculpture. The world is an uncluttered dark-navy background with thin pale mountain-line art, one large quiet halo arc, and a subtle winding trail line. The guardian has no realistic fur, feather, scale, or material texture. Use one planning-level neon contour light and a small muted-gold lineage mark on its shoulder or equivalent body area. The guardian is the clear focal point.

Lineage reference:
<Describe the approved master guardian, its anatomy, markings, and materials. Include an approved visual reference when possible. Keep the Reference Lock background and composition unchanged.>

Planning-level variation:
<Use exactly one Macro, Mezzo, Micro, or Session description from the table above.>

Constraints:
No text, logos, watermark, card frame, humans, copyrighted character resemblance, realistic fur or feathers, surface texture, detailed shading, armour, rock plates, stone, hard faceting, loose sketch lines, visible brushwork, painterly texture, plastic sheen, dominant geometric structures, or busy natural scenery. Preserve the approved guardian's anatomy, background world, planning-level contour color, and gold lineage mark.
```

## Controlled Iteration

1. Approve one Macro master image for a visual family.
2. Use that master image as a reference for each descendant render.
3. Change only the planning-level variation: age, pose, and neon accent color.
4. Review the four images side by side for recognisable family traits and instant planning-level recognition.
5. Revise one variable at a time. Do not generate production assets or update the app until the pilot is approved.

## Avoid

- Copying Pokemon, Yu-Gi-Oh!, or any existing game card character, artwork, layout, or logo.
- Treating every Macro card as an ibex or any other single species.
- Making the image's background so detailed that it competes with coaching content.
- Using large fixed triangles, gates, rings, or other geometry as the main planning-level identifier.
- Generating several permanent versions for a card to represent every valid coaching relationship.
