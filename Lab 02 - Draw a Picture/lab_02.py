# Import the "arcade" library
import arcade

# Open up a window
arcade.open_window (800, 600, "Master Sword")

# Set the background color
arcade.set_background_color (arcade.color.LIGHT_BLUE)

# Start drawing
arcade.start_render ()

# Draw the grass
arcade.draw_lrtb_rectangle_filled (0, 800, 350, 0, arcade.color.DARK_GREEN)

# Draw the pedestal
arcade.draw_polygon_filled ([[200, 20], [600, 20], [550, 100], [250, 100]], arcade.color.GRAY)
arcade.draw_triangle_filled (350, 30, 450, 30, 400, 90, arcade.color.BLACK_OLIVE)
arcade.draw_triangle_filled (400, 30, 375, 60, 425, 60, arcade.color.GRAY)
arcade.draw_polygon_filled ([[200, 20], [250, 100], [270, 200], [220, 100]], arcade.color.BLACK_OLIVE)
arcade.draw_polygon_filled ([[600, 20], [550, 100], [530, 200], [580, 100]], arcade.color.BLACK_OLIVE)
arcade.draw_polygon_filled ([[550, 100], [530, 200], [270, 200], [250, 100]], arcade.color.DARK_GRAY)

# Draw the sword
arcade.draw_polygon_filled ([[380, 155], [385, 150], [415, 150], [420, 155], [430, 400], [370, 400]], arcade.color.LIGHT_GRAY)
arcade.draw_polygon_filled ([[399, 150], [397, 400], [403, 400], [401, 150]], arcade.color.WHITE)
arcade.draw_polygon_filled ([[380, 155], [370, 400], [375, 400], [385, 150]], arcade.color.GRAY)
arcade.draw_polygon_filled ([[420, 155], [430, 400], [425, 400], [415, 150]], arcade.color.GRAY)
arcade.draw_ellipse_filled (400, 400, 200, 35, arcade.color.BLUE, 0, -1)
arcade.draw_ellipse_filled (400, 408, 40, 20, arcade.color.DARK_BLUE, 0, -1)
arcade.draw_ellipse_filled (400, 410, 21, 10, arcade.color.BLUE, 0, -1)
arcade.draw_lrtb_rectangle_filled (390, 410, 550, 410, arcade.color.BLUE)
arcade.draw_triangle_filled (385, 550, 415, 550, 400, 580, arcade.color.BLUE)
arcade.draw_polygon_filled ([[385, 550], [415, 550], [410, 540], [390, 540]], arcade.color.DARK_BLUE)
arcade.draw_polygon_filled ([[390, 540], [390, 530], [410, 510], [410, 520]], arcade.color.PURPLE)
arcade.draw_polygon_filled ([[410, 540], [410, 530], [390, 510], [390, 520]], arcade.color.GREEN)
arcade.draw_polygon_filled ([[410, 510], [410, 500], [390, 480], [390, 490]], arcade.color.GREEN)
arcade.draw_polygon_filled ([[390, 510], [390, 500], [410, 480], [410, 490]], arcade.color.PURPLE)
arcade.draw_polygon_filled ([[390, 480], [390, 470], [410, 450], [410, 460]], arcade.color.PURPLE)
arcade.draw_polygon_filled ([[410, 480], [410, 470], [390, 450], [390, 460]], arcade.color.GREEN)
arcade.draw_polygon_filled ([[410, 450], [410, 440], [390, 420], [390, 430]], arcade.color.GREEN)
arcade.draw_polygon_filled ([[390, 450], [390, 440], [410, 420], [410, 430]], arcade.color.PURPLE)

# Draw the clouds
arcade.draw_ellipse_filled (220, 550, 200, 30, arcade.color.WHITE)
arcade.draw_ellipse_filled (650, 450, 200, 50, arcade.color.WHITE)
arcade.draw_ellipse_filled (610, 480, 200, 65, arcade.color.WHITE)

# Draw de enemy
arcade.draw_ellipse_filled (150, 220, 25, 30, arcade.color.DARK_ORANGE)
arcade.draw_ellipse_filled (170, 230, 30, 20, arcade.color.DARK_ORANGE)
arcade.draw_ellipse_filled (130, 230, 30, 20, arcade.color.DARK_ORANGE)
arcade.draw_ellipse_filled (150, 275, 60, 100, arcade.color.ORANGE)
arcade.draw_ellipse_filled (133, 300, 20, 30, arcade.color.PURPLE)
arcade.draw_ellipse_filled (133, 300, 13, 23, arcade.color.WHITE)
arcade.draw_ellipse_filled (130, 300, 5, 9, arcade.color.BLACK)
arcade.draw_ellipse_filled (167, 300, 20, 30, arcade.color.PURPLE)
arcade.draw_ellipse_filled (167, 300, 13, 23, arcade.color.WHITE)
arcade.draw_ellipse_filled (170, 300, 5, 9, arcade.color.BLACK)
arcade.draw_ellipse_filled (150, 270, 45, 5, arcade.color.PURPLE)

# Finish drawing
arcade.finish_render ()

# Keep the window up until someone closes it
arcade.run ()
