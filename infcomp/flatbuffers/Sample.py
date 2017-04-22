# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class Sample(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSample(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Sample()
        x.Init(buf, n + offset)
        return x

    # Sample
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Sample
    def Time(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Sample
    def Address(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # Sample
    def Instance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Sample
    def DistributionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Sample
    def Distribution(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # Sample
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .NDArray import NDArray
            obj = NDArray()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def SampleStart(builder): builder.StartObject(6)
def SampleAddTime(builder, time): builder.PrependInt32Slot(0, time, 0)
def SampleAddAddress(builder, address): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(address), 0)
def SampleAddInstance(builder, instance): builder.PrependInt32Slot(2, instance, 0)
def SampleAddDistributionType(builder, distributionType): builder.PrependUint8Slot(3, distributionType, 0)
def SampleAddDistribution(builder, distribution): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(distribution), 0)
def SampleAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def SampleEnd(builder): return builder.EndObject()
