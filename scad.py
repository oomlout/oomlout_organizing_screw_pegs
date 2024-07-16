import copy
import opsc
import oobb
import oobb_base

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        filter = ""
        #filter = "flange"

        #kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        kwargs["overwrite"] = True
        
        kwargs["modes"] = ["3dpr", "laser", "true"]
        #kwargs["modes"] = ["3dpr"]
        #kwargs["modes"] = ["laser"]

    # default variables
    if True:
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 6

    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        part_default = {} 
        part_default["project_name"] = "oomlout_organizing_screw_pegs" ####### neeeds setting
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        thickness = 85
        diam = 15
        p3["thickness"] = thickness               
        p3["radius"] = diam/2        
        part["kwargs"] = p3
        part["name"] = f"base_{diam}"        
        #parts.append(part)

        

        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        thickness = 12
        diam = 20
        flange_extra = 6
        flange_depth = 3
        p3["thickness"] = thickness               
        p3["radius"] = diam/2        
        p3["flange_extra"] = flange_extra
        p3["flange_depth"] = flange_depth
        
        part["kwargs"] = p3
        part["name"] = f"base_flange_{diam}_flange_extra_{flange_extra}_flange_depth_{flange_depth}"        
        #parts.append(part)

        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        thickness = 12
        diam = 20
        flange_extra = 6
        flange_depth = 3
        p3["thickness"] = thickness               
        p3["radius"] = diam/2        
        flat_length = 10
        p3["flat_length"] = flat_length
        p3["flange_extra"] = flange_extra
        p3["flange_depth"] = flange_depth        
        part["kwargs"] = p3
        part["name"] = f"base_flange_{diam}_flange_extra_{flange_extra}_flange_depth_{flange_depth}_flat_length_{flat_length}"        
        parts.append(part)
        
        
    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")
            if filter in name:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                print(f"done {part['name']}")
            else:
                print(f"skipping {part['name']}")

def get_base(thing, **kwargs):

    depth = kwargs.get("thickness", 4)
    radius = kwargs.get("radius", 10)
    prepare_print = kwargs.get("prepare_print", False)

    #
    flange_extra = kwargs.get("flange_extra", 0)
    flange_depth = kwargs.get("flange_depth", 0)
    flat_length = kwargs.get("flat_length", 0)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add cylinder
    if flat_length == 0:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"    
        p3["depth"] = depth
        p3["radius"] = radius
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        p3["zz"] = "top"
        oobb_base.append_full(thing,**p3)
        #add flange if flange extra is set
        if flange_extra > 0:            
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "p"
            p3["shape"] = f"oobb_cylinder"    
            p3["depth"] = flange_depth
            p3["radius"] = radius + flange_extra/2
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            p3["pos"] = pos1
            p3["zz"] = "top"
            oobb_base.append_full(thing,**p3)
    else:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"rounded_rectangle"    
        wid = radius*2 + flat_length
        hei = radius*2
        dep = depth
        size = [wid, hei, dep]
        p3["size"] = size
        p3["radius"] = radius        
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += -dep
        p3["pos"] = pos1
        p3["zz"] = "top"
        oobb_base.append_full(thing,**p3)
        #add flange if flange extra is set
        if flange_extra > 0:            
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "p"
            p3["shape"] = f"rounded_rectangle"    
            wid = radius*2 + flat_length + flange_extra
            hei = radius*2 + flange_extra
            dep = flange_depth
            size = [wid, hei, dep]
            p3["size"] = size
            #p3["radius"] = radius + flange_extra/2            
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            pos1[2] += -dep
            p3["pos"] = pos1            
            oobb_base.append_full(thing,**p3)


    #add holes
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_screw_countersunk"    
    p3["depth"] = depth
    p3["radius_name"] = "m4_screw_wood"
    p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)
    
###### utilities



def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
    
    #func = globals()[f"get_{name}"]
    #func(thing, **kwargs)

    get_base(thing, **kwargs)

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        opsc.opsc_make_object(f'scad_output/{thing["id"]}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)    


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)