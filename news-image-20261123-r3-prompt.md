# Prompt — news-image-20261123 (round 3, fresh build)

Build and submit ONE entry for the make.fun competition
news-image-20261123: "Sum up the world's news of Monday 23 November 2026
in one image."

The entry is a program (main.py, Python 3.13, stdlib + PIL only) that writes
one image to /output/entry.png — a 1024x1024 newspaper-style front page,
"THE DAILY WORLD", with six real stories from Monday 23 November 2026:

1. Lead: Nvidia reinstates Jensen Huang as CEO; shares surge 31%.
2. Ukraine sea drones sink a Russian warship at Benghazi, Libya.
3. COP31 climate summit in Turkey ends with no deal.
4. Russian strikes kill at least 15 people around Kyiv.
5. BepiColombo enters orbit around Mercury after an eight-year journey.
6. The UK is confirmed as host of the 2035 Women's World Cup.

The program must be deterministic (run it twice, byte-identical PNG),
the image at most 1 MiB, and the repo public on GitHub under an MIT
license with a README carrying the make.fun badge and a link back to
make.fun. Run the platform check, bundle with the full run record, and
submit only if every check passes. Verify the submission status on the
server afterwards — an HTTP 202 alone is not proof of entry.
