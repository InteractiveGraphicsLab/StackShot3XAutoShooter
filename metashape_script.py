# MetashapeのPython APIを使用
# referenced from https://www.agisoft.com/pdf/metashape_python_api_2_0_0.pdf

import os
import Metashape

env = os.environ

# check is activated license !!
# Metashape.License().activate()

Metashape.app.cpu_enable = False
Metashape.app.gpu_mask = 1 ##

doc = Metashape.Document()
project_dir = env['METASHAPE_PROJECT_PATH']

# 結果保存用のファイルを作成
doc.save(path=os.path.join(project_dir, 'project.psz'))

chunk = doc.addChunk()
photos = []
for img in os.listdir(env['IMAGE_PATH']):
    photos.append(os.path.join(env['IMAGE_PATH'], img))

chunk.addPhotos(photos)

# Align Photos
# アライメントに失敗したら、精度を落として再実行を繰り返す
print("Align Photos...")
for d in [0, 1, 2, 4, 8]:
    chunk.matchPhotos(downscale=d, generic_preselection=True, reference_preselection=False, keypoint_limit=40000, tiepoint_limit=4000)
    chunk.alignCameras()

    total_cameras = len([cam for cam in chunk.cameras])
    align_cameras = len([cam for cam in chunk.cameras if cam.transform])
    align_prcntg = (float(align_cameras) / float(total_cameras)) * 100.0 # アライメント成功率を計算

    print("Total cameras: {}".format(total_cameras))
    print("Align cameras: {}".format(align_cameras))
    print("Alignment Percentage: {}%".format(align_prcntg))

    if align_prcntg > 90.0:
        print("Alignment was succesfull(accuracy {}) - {}%, continue processing...".format(d, align_prcntg))
        break

    print(50 * '=')
    print("Could not align images using the desired accuracy value : {}".format(d))
    print("Trying again with degraded accuracy...")

    for camera in chunk.cameras:
        camera.transform = None
    chunk.point_cloud = None

# Build DepthMaps
print("Build Depth Maps...")
chunk.buildDepthMaps(downscale=1, filter_mode=Metashape.FilterMode.MildFiltering, reuse_depth=False)

# Build Mesh
print("Build Mesh...")
chunk.buildModel(surface_type=Metashape.SurfaceType.Arbitrary, interpolation=Metashape.Interpolation.EnabledInterpolation, \
                 face_count=Metashape.FaceCount.HighFaceCount, source_data=Metashape.DataSource.DepthMapsData, vertex_colors=True, volumetric_masks=False)

# Build UV
print("Build UV...")
chunk.buildUV(mapping_mode=Metashape.MappingMode.GenericMapping, page_count=1, texture_size=8192)

# Build Texture
print("Build Texture...")
chunk.buildTexture(blending_mode=Metashape.BlendingMode.MosaicBlending, texture_size=8192, fill_holes=True, ghosting_filter=True, \
                   texture_type=Metashape.Model.TextureType.DiffuseMap, transfer_texture=False)

doc.save()
