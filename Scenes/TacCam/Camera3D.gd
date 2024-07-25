extends Camera3D

var RAY_RANGE = 2000

func get_camera_collision():
	var mouse_pos = get_viewport().get_mouse_position()
	
	var ray_origin = project_ray_origin(mouse_pos)
	var ray_end = ray_origin + project_ray_normal(mouse_pos)*RAY_RANGE
	
	var ray = PhysicsRayQueryParameters3D.create(ray_origin,ray_end)
	var intersection = get_world_3d().direct_space_state.intersect_ray(ray)
	
	return intersection
