# labelsUnityPython
Code for generating labels for the synthesised black/white greyscale images. Where per overall image, there is a black/white image per object of interest.
Code that outputs the min/max x/y locations of white pixels on the image in YOLOv5 format into txt files. 
This is supplementary code that goes along with the cones generation image generation format of the Unity repo. 

The white pixels on black background represent the visible region of a cone. A label is then drawn as a bounding box of these pixels. The cone colour is passed to the label from the file name originally created by Unity. 
For every image with multiple cones on it, black/white images of individual cones are generated. This code outputs a .txt of all cones file per main image. 
For images with no cones on them, empty .txt files are generated. 


List of Unity Asset Store assets used in this project: 
• Traffic cones - https://assetstore.unity.com/packages/3d/props/traffic-cones-34912
• Ground materials - https://assetstore.unity.com/packages/2d/textures-materials/floors/yughues-free-ground-materials-13001
• Concrete materials - https://assetstore.unity.com/packages/2d/textures-materials/concrete/yughues-free-concrete-materials-12951#content
• Asphalt materials - https://assetstore.unity.com/packages/2d/textures-materials/roads/asphalt-materials-141036
• Skyboxes - https://assetstore.unity.com/packages/2d/textures-materials/sky/allsky-free-10-sky-skybox-set-146014,
             https://assetstore.unity.com/packages/2d/textures-materials/sky/8k-skybox-pack-free-150926
• Birch Trees - https://assetstore.unity.com/packages/3d/vegetation/trees/birch-tree-pack-vol-1-49093
• Green trees - https://assetstore.unity.com/packages/3d/vegetation/trees/realistic-tree-9-rainbow-tree-54622,
                https://assetstore.unity.com/packages/3d/vegetation/trees/realistic-tree-10-54724
• Colourful trees - https://assetstore.unity.com/packages/vfx/shaders/world-space-trees-free-shader-117088
• White/Red Barriers - https://assetstore.unity.com/packages/3d/props/exterior/old-plastic-barrier-182509
• Various road props - https://assetstore.unity.com/packages/3d/props/exterior/road-props-low-poly-123340
• 2 road blockers - https://assetstore.unity.com/packages/3d/props/exterior/road-blocker-663
• Industrial buildings - https://assetstore.unity.com/packages/3d/building-shed-1042, 
                         https://assetstore.unity.com/packages/3d/environments/industrial/storage-building-50430,
                         https://assetstore.unity.com/packages/3d/environments/industrial/free-industrial-building-garage-123146
• Cars - https://assetstore.unity.com/packages/3d/vehicles/land/hq-racing-car-model-no-1203-139221, 
         https://assetstore.unity.com/packages/3d/vehicles/low-poly-car-149312, 
         https://assetstore.unity.com/packages/3d/vehicles/land/low-poly-sports-car-20-144253, 
         https://assetstore.unity.com/packages/3d/vehicles/land/modern-touring-car-pack-demo-132820, 
         https://assetstore.unity.com/packages/3d/vehicles/land/touring-race-car-pack-demo-130064
• Race tracks - https://assetstore.unity.com/packages/3d/environments/roadways/race-tracks-140501
