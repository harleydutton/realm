extends CharacterBody3D

@onready var agent = $NavigationAgent3D
@onready var cam = $TacCam/SpringArm3D/Camera3D
const SPEED = 5.0
const JUMP_VELOCITY = 4.5
var state = "normal" #this should probably be an enum

# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")

func _physics_process(delta):
	var cur_loc = global_transform.origin
	var next_loc = agent.get_next_path_position()
	var new_vel = (next_loc - cur_loc).normalized() * SPEED
	velocity = new_vel
	move_and_slide()

func _input(event):
	if Input.is_action_pressed("click") && state == "normal":
		var intersection = cam.get_camera_collision()
		if intersection:
			move_to(intersection.collider.position+intersection.normal)

func move_to(target):
	agent.set_target_position(target)
	
