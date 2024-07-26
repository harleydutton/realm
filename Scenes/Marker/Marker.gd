extends Node3D

@onready var cam = $"../CameraRig/SpringArm3D/Camera3D"
@onready var page = $"../Page"

func _input(_event):
	if Input.is_action_pressed("click"):
		var intersection = cam.get_camera_collision()
		if intersection:
			position = intersection.collider.position+intersection.normal
			#page.add(position)
			#print(position)
