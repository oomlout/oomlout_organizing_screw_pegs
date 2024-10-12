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
        filter = "multi"
        #filter = "flange"

        kwargs["save_type"] = "none"
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
        part_default["project_name"] = "oomlout_organizing_screw_peg" ####### neeeds setting
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

        
        # standard sphere ones
        if True:
            thicknesses = [12]
            diams = [20]
            flange_extras = [6]
            flange_depths = [3]

            for thickness in thicknesses:
                for diam in diams:
                    for flange_extra in flange_extras:
                        for flange_depth in flange_depths:
                            part = copy.deepcopy(part_default)
                            p3 = copy.deepcopy(kwargs)
                            
                            p3["thickness"] = thickness               
                            p3["radius"] = diam/2        
                            p3["flange_extra"] = flange_extra
                            p3["flange_depth"] = flange_depth
                            
                            part["kwargs"] = p3
                            part["name"] = f"base_flange_{diam}_flange_extra_{flange_extra}_flange_depth_{flange_depth}"        
                            parts.append(part)

        # multi hole ones
        if True:
            thicknesses = [30]
            diams = [20]
            flange_extras = [15]
            flange_depths = [6]

            for thickness in thicknesses:
                for diam in diams:
                    for flange_extra in flange_extras:
                        for flange_depth in flange_depths:
                            part = copy.deepcopy(part_default)
                            p3 = copy.deepcopy(kwargs)
                            
                            p3["thickness"] = thickness               
                            p3["radius"] = diam/2        
                            p3["flange_extra"] = flange_extra
                            p3["flange_depth"] = flange_depth
                            multi_hole = 3
                            p3["multi_hole"] = multi_hole                        
                            part["kwargs"] = p3
                            part["name"] = f"base_flange_{diam}_flange_extra_{flange_extra}_flange_depth_{flange_depth}_multi_hole_{multi_hole}"        
                            parts.append(part)


        
        # flat ones
        if True:
            thicknesses = [15]
            diams = [20]
            flange_extras = [6]
            flange_depths = [3]
            flat_lengths = [10]

            for thickness in thicknesses:
                for diam in diams:
                    for flange_extra in flange_extras:
                        for flange_depth in flange_depths:                        
                            for flat_length in flat_lengths:                                
                                part = copy.deepcopy(part_default)
                                p3 = copy.deepcopy(kwargs)
                                p3["thickness"] = thickness               
                                p3["radius"] = diam/2        
                                
                                p3["flat_length"] = flat_length
                                p3["flange_extra"] = flange_extra
                                p3["flange_depth"] = flange_depth        
                                part["kwargs"] = p3
                                part["name"] = f"base_flange_{diam}_flange_extra_{flange_extra}_flange_depth_{flange_depth}_flat_length_{flat_length}_depth_{thickness}"        
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
    multi_hole = kwargs.get("multi_hole", 1)

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
    if True:
        if multi_hole == 1:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_screw_countersunk"    
            p3["depth"] = depth
            p3["radius_name"] = "m4_screw_wood"
            p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            p3["pos"] = pos1
            oobb_base.append_full(thing,**p3)
        if multi_hole == 3:
            
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_screw_countersunk"    
            p3["depth"] = depth
            p3["radius_name"] = "m4_screw_wood"
            p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            
            import math          
            shift = 6
            pos11 = copy.deepcopy(pos1)
            angle = 0
            pos11[0] += math.cos(math.radians(angle))*shift
            pos11[1] += math.sin(math.radians(angle))*shift
            pos12 = copy.deepcopy(pos1)
            angle = 120
            pos12[0] += math.cos(math.radians(angle))*shift
            pos12[1] += math.sin(math.radians(angle))*shift
            pos13 = copy.deepcopy(pos1)
            angle = 240
            pos13[0] += math.cos(math.radians(angle))*shift
            pos13[1] += math.sin(math.radians(angle))*shift
            

            poss = []
            poss.append(pos11)
            poss.append(pos12)
            poss.append(pos13)


            p3["pos"] = poss
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