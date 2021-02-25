using UnityEditor;
using System.IO;
using System.Collections.Generic;
using UnityEngine;

public class TestAssetBundle
{
    [MenuItem("AB/buildAB")]
    public static void TestBuildAb()
    {
        string buildPath = "Assets/AssetBundles";
        if (!Directory.Exists(buildPath))
        {
            Directory.CreateDirectory(buildPath);
        }

        BuildPipeline.BuildAssetBundles(buildPath, BuildAssetBundleOptions.ChunkBasedCompression, BuildTarget.StandaloneWindows);
    }
}