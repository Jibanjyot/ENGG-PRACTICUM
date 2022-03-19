import pyDSA_core as dsa
import matplotlib.pyplot as plt


# Import an image
im = dsa.import_from_image('static/uploads/droplet.jpg', dx=1/120,
                           dy=1/120, unit_x='mm', unit_y='mm')

# Display it
# plt.figure()
# im.display()
# plt.show()

# im.set_baseline(pt1=[0, 0], pt2=[5, 0])
edge = im.edge_detection()
edge_cont = im.edge_detection_contour(level=.25)
sfit = edge.fit_spline()
plt.figure()
im.display()
edge_cont.display()
plt.show()

sfit.compute_contact_angle()
print('Contact angles: {}'.format(sfit.thetas))

radius = sfit.get_base_diameter()
print("\n=== Drop base diameter: ===")
print(radius)

height = sfit.get_drop_height()
print("\n=== Drop height: ===")
print(height)

volume = sfit.get_drop_volume()
print("\n=== Drop Volume: ===")
print(volume)
