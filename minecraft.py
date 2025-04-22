from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()
window.borderless = False
window.title = 'MiniCraft by Hasan Hayat'
window.fps_counter.enabled = True

# Using public domain images from Unsplash for texture simulation (just placeholders)
textures = {
    'grass': load_texture('https://images.unsplash.com/photo-1606788075761-4b89a5c93000?fit=crop&w=200&q=80'),
    'stone': load_texture('https://images.unsplash.com/photo-1558591719-1b8490b579e0?fit=crop&w=200&q=80'),
    'brick': load_texture('https://images.unsplash.com/photo-1589927986089-35812388d1d7?fit=crop&w=200&q=80'),
    'dirt': load_texture('https://images.unsplash.com/photo-1619718074091-952d2e68cb10?fit=crop&w=200&q=80'),
}

block_pick = 'grass'

def update():
    global block_pick
    if held_keys['1']: block_pick = 'grass'
    if held_keys['2']: block_pick = 'stone'
    if held_keys['3']: block_pick = 'brick'
    if held_keys['4']: block_pick = 'dirt'

class Voxel(Button):
    def __init__(self, position=(0,0,0), texture='grass'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=textures[texture],
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxels.append(Voxel(position=self.position + mouse.normal, texture=block_pick))
            if key == 'right mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture='sky_default',
            scale=150,
            double_sided=True
        )

voxels = []
for z in range(8):
    for x in range(8):
        voxels.append(Voxel(position=(x,0,z), texture='grass'))

player = FirstPersonController()
sky = Sky()

app.run()


