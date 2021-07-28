import realcel.color_utils as color

class TestColorUtils:
    def test_it_finds_the_distance_between_two_colors(self):
        colors = [
            ((0, 0, 0), (0, 0, 0)),
            ((255, 255, 255), (255, 255, 255)),
            ((0, 0, 0), (255, 255, 255)),
            ((194, 210, 231), (73, 100, 105))
        ]

        distances = [
            0.00,
            0.00,
            441.67,
            206.44,
        ]

        for i in range(len(colors)):
            assert color.distance(colors[i][0], colors[i][1]) == distances[i]

    def test_it_converts_rgb_to_hsl(self):
        rgb = [
            (0,0,0),
            (255,255,255),
            (255,0,0),
            (0,255,0),
            (0,0,255),
            (255,255,0),
            (0,255,255),
            (255,0,255),
            (191,191,191),
            (128,128,128),
            (128,0,0),
            (128,128,0),
            (0,128,0),
            (128,0,128),
            (0,128,128),
            (0,0,128),
            (66,135,245),
            (102,90,41),
        ]

        hsl = [
            (0,0,0),
            (0,0,1),
            (0,1,.5),
            (120,1,.5),
            (240,1,.5),
            (60,1,.5),
            (180,1,.5),
            (300,1,.5),
            (0,0,.75),
            (0,0,.5),
            (0,1,.25),
            (60,1,.25),
            (120,1,.25),
            (300,1,.25),
            (180,1,.25),
            (240,1,.25),
            (217,.9,.61),
            (48,.43,.28),
        ]

        for i in range(len(rgb)):
            assert color.to_hsl(rgb[i]) == hsl[i]

    def test_it_converts_from_hsl_to_rgb(self):
        rgb = [
            (0,0,0),
            (255,255,255),
            (255,0,0),
            (0,255,0),
            (0,0,255),
            (255,255,0),
            (0,255,255),
            (255,0,255),
            (191,191,191),
            (128,128,128),
            (128,0,0),
            (128,128,0),
            (0,128,0),
            (128,0,128),
            (0,128,128),
            (0,0,128),
            (66,135,245),
            (102,90,41),
        ]

        hsl = [
            (0,0,0),
            (0,0,1),
            (0,1,.5),
            (120,1,.5),
            (240,1,.5),
            (60,1,.5),
            (180,1,.5),
            (300,1,.5),
            (0,0,.75),
            (0,0,.5),
            (0,1,.25),
            (60,1,.25),
            (120,1,.25),
            (300,1,.25),
            (180,1,.25),
            (240,1,.25),
            (217,.9,.61),
            (48,.43,.28),
        ]

        for i in range(len(rgb)):
            assert color.to_rgb(hsl[i]) == rgb[i]

    # Written to test a curiousity about the algorithm I found. Takes waay to long
    # to be part of the normal test suite, but it to_hsl function is edited, it would
    # be nice to be sure it still follows this standard.
    # def test_it_never_picks_a_value_outside_expected_range(self):
    #     for r in range(255):
    #         for g in range(255):
    #             for b in range(255):
    #                 (h, s, l) = color.to_hsl((r, g, b))
    #                 assert h >= 0 and h <= 360
    #                 assert s >= 0 and s <= 1
    #                 assert l >= 0 and l <= 1
