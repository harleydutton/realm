using Godot;
using System;
using System.Collections.Generic;

public partial class Page : Node{
	private static PackedScene packedVoxel = ResourceLoader.Load<PackedScene>("res://Scenes/Page/Voxel.tscn");
	public List<Node3D> voxels;
	
	public Page(){
		voxels = new List<Node3D>();
	}
	
	public override void _Ready()
	{
		add(new Vector3(0,0,0));
	}
	
	public void add(Vector3 pos){
		Node3D instance = (Node3D)packedVoxel.Instantiate();
		instance.Position = pos;
		voxels.Add(instance);
		AddChild(instance);
	}
	
	public float dist(Vector3 a, Vector3 b){
		return (a-b).Length();
	}
	
	public int[] bounds(Node3D[] players){
		return void;
	}

}
