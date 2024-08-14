using Godot;
using System;
using System.Collections.Generic;

public partial class Page : Node{
	private static PackedScene packedVoxel = ResourceLoader.Load<PackedScene>("res://Scenes/Page/Voxel.tscn");
	public List<Node3D> voxels;

	public static int procGenDist = 10;
	
	public Page(){
		voxels = new List<Node3D>();
	}
	
	public override void _Ready()
	{
		make_floor(new Vector3(0,0,0));
	}
	
	public void make_floor(Vector3 pos){
		for(int x = (int)pos[0]-procGenDist; x < (int)pos[0]+procGenDist; x++){
			for(int y = (int)pos[1]-procGenDist; y < (int)pos[1]+procGenDist; y++){
				for(int z = (int)pos[2]-procGenDist; z < (int)pos[2]+procGenDist; z++){
					if(y < pos[2]){
						add(new Vector3(x,y,z));
					}
				}
			}
		}
	}
	
	public void add(Vector3 pos){
		Node3D instance = (Node3D)packedVoxel.Instantiate();
		instance.Position = pos;
		voxels.Add(instance);
		AddChild(instance);
	}
}
