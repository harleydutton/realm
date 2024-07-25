using Godot;
using System;

public partial class Location : Node3D
{
	public Location(int x,int y,int z){
		this.x = x;
		this.y = y;
		this.z = z;
	}
	public int x {get;}
	public int y {get;}
	public int z {get;}
}
