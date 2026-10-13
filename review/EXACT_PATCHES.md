# Exact correction review — https://mississippideltareport.com

Read-only authenticated preflight. No WordPress writes or media uploads performed.

The JSON receipt binds each post identity, original revision, raw fields and proposed payload to SHA-256 hashes. Any later apply must re-read and compare the full before snapshot; stop on a mismatch or 403. Preserve dates, slugs, authors, statuses, categories, tags, media and all unlisted fields.

## Managed account

{"capabilities": {"edit_others_posts": true, "edit_posts": true, "edit_published_posts": true, "upload_files": true}, "id": 1}

Capability checks support eligibility; actual REST writes are unverified.

## Post 18040

https://mississippideltareport.com/news/dense-fog-could-reduce-visibility-to-half-a-mile-overnight-and-early-wednesday-morning/13/10/2026/

- Before snapshot SHA-256: `2dba73eb4097a502552f5bb7224aff55dcae8ab25a5f39ce86c52b034ebc60e6`
- Payload SHA-256: `1ec9132a792cca8d9d13eaa7705aadc2150a5a7b63b6e20070043e187438113d`
- Proposed snapshot SHA-256: `58ceefe28e066d64533f83f206060026cd08c22e4938aba76b6493d0988bc74f`
- Existing author ID: 1; owned by account: True
- Ready: True

### title

```diff
--- before
+++ proposed
@@ -1 +1 @@
-Dense fog could reduce visibility to half a mile overnight and early Wednesday morning+NWS forecast called for dense fog Tuesday morning, Oct. 13
```

### excerpt

```diff
--- before
+++ proposed
@@ -1 +1 @@
-Patchy dense fog is expected to reduce visibility across the Highway 84 corridor late tonight and early Wednesday morning, prompting caution for drivers.+The National Weather Service forecast patchy dense fog along the Highway 84 corridor from 5 to 9 a.m. Tuesday, Oct. 13.
```

### content

```diff
--- before
+++ proposed
@@ -1,3 +1,4 @@
-<p>Patchy dense fog is expected to develop late tonight across the Highway 84 corridor, reducing visibility to half a mile or less, according to the National Weather Service.</p> <p>The fog is forecast to persist between 5 a.m. and 9 a.m. Wednesday, affecting morning commuters. Drivers are urged to slow down and use low beam headlights in areas of dense fog to improve safety.</p> <p>Officials advise motorists to exercise caution and allow extra time for travel during this period. No other weather warnings have been issued at this time.</p>
-
-<p><em>Source: <a href="https://www.facebook.com/330424809127534/posts/1535789241924412" target="_blank" rel="noopener">Original Article</a></em></p>+<p>The National Weather Service forecast patchy dense fog along the Highway 84 corridor between 5 and 9 a.m. Tuesday, Oct. 13, with visibility potentially falling to half a mile or less.</p>
+<p>The agency urged drivers encountering fog to slow down, use low-beam headlights and allow extra travel time.</p>
+<p><em>Correction (Oct. 13, 2026): The forecast applied to Tuesday morning, not Wednesday morning.</em></p>
+<p><em>Source: <a href="https://www.facebook.com/NWSJacksonMS/posts/1535789241924412/">National Weather Service Jackson</a></em></p>
```

### Sources and scope

- https://www.facebook.com/NWSJacksonMS/posts/1535789241924412/
Independently viewed original graphic: Tue Oct13 2026, 12:09AM issuance, 5AM–9AM Tuesday; forecast not observed conditions.

## Post 17980

https://mississippideltareport.com/news/greenville-mississippi-claims-states-only-top-10-ranking/11/10/2026/

- Before snapshot SHA-256: `1eb206c859fb4e63c74bd506b3e871d4ed3a79d6670131d8d3252f66e05ef2c2`
- Payload SHA-256: `12b013ed7f7908da217b6f0d0337fc62a4d04df74044363543f4f9d0d68e6ed8`
- Proposed snapshot SHA-256: `e77d0662b07f822be16a18bfc79b6ea24496711be92d33e4b38265440d91cd57`
- Existing author ID: 1; owned by account: True
- Ready: True

### title

```diff
--- before
+++ proposed
@@ -1 +1 @@
-Greenville, Mississippi, claims state’s only top 10 ranking+Doe’s Eat Place in Greenville ranks eighth on Discovery Matt’s Southern restaurant list
```

### excerpt

```diff
--- before
+++ proposed
@@ -1 +1 @@
-Greenville is the only city in Mississippi to make the top ten list, according to local officials and tourism authorities.+A Discovery Matt editorial list places Doe’s Eat Place in Greenville eighth among 35 old-school Southern restaurants.
```

### content

```diff
--- before
+++ proposed
@@ -1,3 +1,4 @@
-<p>Greenville, Mississippi, is the only city in the state to rank in the top ten, according to local sources. The city’s recognition highlights its significance within Mississippi’s tourism and economic landscape.</p> <p>The Mississippi Development Authority, Visit Mississippi, the Greenville-Washington County Convention & Visitors Bureau, Entergy Mississippi, and the city government all acknowledge Greenville's distinction. They emphasize the city’s role as a key destination in the state.</p> <p>Officials say the ranking brings attention to Greenville’s attractions and economic vitality. They also note ongoing efforts to promote tourism and community development in the region.</p>
-
-<p><em>Source: <a href="https://www.facebook.com/1240534114844017/posts/1480442584186501" target="_blank" rel="noopener">Original Article</a></em></p>+<p>Doe’s Eat Place in Greenville is ranked eighth on Discovery Matt’s editorial list of 35 old-school restaurants in the South.</p>
+<p>Delta Compass – WCEA shared the list on Facebook, highlighting Greenville’s entry. The graphic lists Doe’s Eat Place as the only Mississippi restaurant in its top 10.</p>
+<p><em>Correction (Oct. 13, 2026): The list ranks restaurants, not cities. An earlier version also attributed comments to agencies without supporting statements.</em></p>
+<p><em>Source: <a href="https://www.facebook.com/1240534114844017/posts/1480442584186501">Delta Compass – WCEA announcement and ranking graphic</a></em></p>
```

### Sources and scope

- https://www.facebook.com/1240534114844017/posts/1480442584186501
Independently viewed graphic: Doe’s8, Weidmann’s19, TaylorGrocery29; no government endorsement.

## Post 17992

https://mississippideltareport.com/news/mississippi-delta-community-college-to-host-coronation-during-100th-homecoming/12/10/2026/

- Before snapshot SHA-256: `df8320168430e18d35ebcbf4d2c060aee5204d460b5dc7421de30c0915648c17`
- Payload SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Proposed snapshot SHA-256: `df8320168430e18d35ebcbf4d2c060aee5204d460b5dc7421de30c0915648c17`
- Existing author ID: 1; owned by account: True
- Ready: True

No changes proposed. Preserve this duplicate URL and publish status; consolidation remains a separate decision.

### Sources and scope


Preserve duplicate URLs/statuses. No mutation proposed pending separate consolidation/expansion review.

## Post 18020

https://mississippideltareport.com/news/mississippi-delta-community-college-hosts-black-tie-coronation-during-100th-homecoming/12/10/2026/

- Before snapshot SHA-256: `939a4217bd21d66c36694a0160befbc2eccfa9811d881268ddde243336f3481f`
- Payload SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Proposed snapshot SHA-256: `939a4217bd21d66c36694a0160befbc2eccfa9811d881268ddde243336f3481f`
- Existing author ID: 1; owned by account: True
- Ready: True

No changes proposed. Preserve this duplicate URL and publish status; consolidation remains a separate decision.

### Sources and scope


Preserve duplicate URLs/statuses. No mutation proposed pending separate consolidation/expansion review.

## Later application boundary

Use the payload digest to bind approved JSON and the before-snapshot digest to detect concurrent edits. The proposed-snapshot hash is a planning fingerprint, not the expected live rendered response: WordPress rendering must be verified separately after any approved write. No apply route exists on this review branch. After approved verified application, retire any one-shot mutation route created for it.
