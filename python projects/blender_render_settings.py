import bpy 


bl_info = {
       "name": "Easy Render Settings",
       "blender": (3, 0, 0),
       "category": "Object",
   }



class CONTEXT_OT_change_render_engine_cycles(bpy.types.Operator):
    """Just for a testing purposes"""
    bl_idname = 'engine.cycles'
    bl_label = "Cycles"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Create"
    bl_context = "objectmode"
    
    def execute(self, context):
        
       
        bpy.context.scene.render.engine = 'CYCLES'

        return {'FINISHED'}


    

class CONTEXT_OT_change_render_engine_workbench(bpy.types.Operator):
    """Just for a testing purposes"""
    bl_idname = 'engine.workbench'
    bl_label = "Workbench"
    
    def execute(self, context):
        
       
        bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'
        return {'FINISHED'}                                                                                                                                            
    
class CONTEXT_OT_change_render_engine_eevee(bpy.types.Operator):
    """Just for a testing purposes"""
    bl_idname = 'engine.eevee'
    bl_label = "EEVEE"
    
    def execute(self, context):
        # bpy.context.scene.cycles.preview_samples = 512
        bpy.context.scene.render.engine = 'BLENDER_EEVEE'

        return {'FINISHED'}
    



class RENDER_OT_create_render(bpy.types.Operator):

    bl_idname = 'render.image'
    bl_label = "Render"

    def execute(self, context):
        camera = bpy.context.scene.objects.get("Camera")
        if camera:    
            bpy.ops.render.render(write_still = 1)
        else:
           self.report({'INFO'}, "You don't have camera in your scene")

        return {'FINISHED'}



class CONTEXT_OT_starting_preset(bpy.types.Operator):
    bl_idname = 'cycles.preset_starting'        
    bl_label = "Working Preset"

    def execute(self, context):
        bpy.context.scene.cycles.samples = 256
        bpy.context.scene.cycles.preview_samples = 128


        return {'FINISHED'}




class CONTEXT_OT_cycles_final_preset(bpy.types.Operator):
    bl_idname = 'cycles.preset_finish'        
    bl_label = 'Final Preset'

    def execute(self, context):
        bpy.context.scene.cycles.samples = 1024
        bpy.context.scene.cycles.preview_samples = 512

        return {'FINISHED'}
        



class VIEW3D_PT_choose_render(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Graphics'
    bl_label = 'Render'
    bl_idname = 'cycles_starting.settings'
    
    
    def draw(self, context):


        layout = self.layout  

        self.layout.label(text="Choose Your Engine")

        split = layout.split()

        layout = self.layout.operator('engine.cycles')
        layout = self.layout.operator('engine.eevee')
        layout = self.layout.operator('engine.workbench')


        



class VIEW3D_PT_render_settings(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Graphics'
    bl_label = 'Graphic'
    bl_idname = 'render_engines_settings'
    bl_order = 1000
    
    def draw(self, context):
        
        

        if bpy.context.scene.render.engine == 'CYCLES':
            self.layout.label(text="Cycles")

            col = self.layout.column(align = True)
            row = col.row(align=True)
            
            row.prop(context.scene.cycles, 'use_denoising')
            row.prop(context.scene.cycles, 'use_preview_denoising')

            col = self.layout.column(align = True)
        
            
            
            col = self.layout.column(align = True)
            row_viewport = col.row(align=True)
            
            

            row_viewport.prop(context.scene.cycles, 'preview_samples')
            row_viewport.prop(context.scene.cycles, 'samples')

            col1 = self.layout.column(align = True)

        
        elif bpy.context.scene.render.engine == 'BLENDER_EEVEE':
            self.layout.label(text="EEVEE")   

        else:
            self.layout.label(text="Workbench")
            



        

        col = self.layout.column(align = True)
        row = col.row(align=True)

        row_viewport2 = col.row(align=True)
        row_viewport3 = col.row(align=True)
        row_viewport4 = col.row(align=True)


        row_viewport2.prop(context.scene.render, 'resolution_x')
        row_viewport3.prop(context.scene.render, 'resolution_y')
        
    
        col = self.layout.column(align = True)
        col.prop(context.scene.render.image_settings, 'file_format')
        layout = self.layout.operator('render.image')



class VIEW3D_PT_render_passes(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Graphics'
    bl_label = 'Passes'
    bl_idname = 'render_engines_passes'
    bl_order = 200


    def draw(self, context):
        

        if bpy.context.scene.render.engine == 'CYCLES':
            self.layout.label(text="Cycles")
            col = self.layout.column(align = True)

            col.prop(context.scene.view_layers["ViewLayer"], 'use_pass_mist')
            col.prop(context.scene.view_layers["ViewLayer"], 'use_pass_ambient_occlusion')
            col.prop(context.scene.view_layers["ViewLayer"], 'use_pass_environment')
            col.prop(context.scene.view_layers["ViewLayer"], 'use_pass_shadow')
            col.prop(context.scene.view_layers["ViewLayer"], 'use_pass_cryptomatte_object')
            
        elif bpy.context.scene.render.engine == 'BLENDER_EEVEE':
            self.layout.label(text="EEVEE")   
            col = self.layout.column(align = True)

            col.prop(context.scene.view_layers["ViewLayer"], 'use_pass_mist')
            col.prop(context.scene.view_layers["ViewLayer"], 'use_pass_environment')
            col.prop(context.scene.view_layers["ViewLayer"], 'use_pass_ambient_occlusion')



        else:
            pass
             



class VIEW3D_PT_render_presets(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Graphics'
    bl_label = 'Presets'
    bl_idname = 'render_engines_presets'
    bl_order = 100
    
    def draw(self, context):
        
        

        if bpy.context.scene.render.engine == 'CYCLES':
            self.layout.label(text="Cycles")
            
            layout = self.layout.operator('cycles.preset_starting')
            layout = self.layout.operator('cycles.preset_finish')
            
            
        

        
        elif bpy.context.scene.render.engine == 'BLENDER_EEVEE':
            self.layout.label(text="EEVEE")   

        else:
            pass

classes = {    (CONTEXT_OT_change_render_engine_workbench)
    (VIEW3D_PT_choose_render)
    (VIEW3D_PT_render_settings)
    (CONTEXT_OT_change_render_engine_cycles)
    (CONTEXT_OT_change_render_engine_eevee)
    (RENDER_OT_create_render)
    (CONTEXT_OT_starting_preset)
    (CONTEXT_OT_cycles_final_preset)
    (VIEW3D_PT_render_passes)
    (VIEW3D_PT_render_presets)
}
def register():
    classes    
def unregister():
    classes 
if __name__ == '__main__':
    register() 
